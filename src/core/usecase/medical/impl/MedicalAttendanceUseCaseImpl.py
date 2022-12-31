from src.core.usecase.medical.MedicalAttendanceUseCase import MedicalAttendanceUseCase
from src.core.usecase.utils import HttpResponse
from src.core.usecase.utils import MyCustomError
from src.core.usecase.utils import DateFormat
from src.core.dataprovider.repository.medical.CreateMedicalAttendance import CreateMedicalAttendance
from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.core.dataprovider.repository.pathology.FindByPathologyByPatientId import FindByPathologyByPatientId
from src.core.dataprovider.repository.medical.FindMedicalAttendanceByDate import FindMedicalAttendanceByDate
from src.core.domain.MedicalAttendance import MedicalAttendance


class MedicalAttendanceUseCaseImpl(MedicalAttendanceUseCase):
    __create_medical_attendance: CreateMedicalAttendance
    __find_patient_by_id: FindPatientById
    __find_by_pathology_by_patient_id: FindByPathologyByPatientId
    __find_medical_attendance_by_date: FindMedicalAttendanceByDate

    def __init__(self,
                 create_medical_attendance: CreateMedicalAttendance,
                 find_patient_by_id: FindPatientById,
                 find_by_pathology_by_patient_id: FindByPathologyByPatientId,
                 find_medical_attendance_by_date: FindMedicalAttendanceByDate) -> None:
        self.__create_medical_attendance = create_medical_attendance
        self.__find_patient_by_id = find_patient_by_id
        self.__find_by_pathology_by_patient_id = find_by_pathology_by_patient_id
        self.__find_medical_attendance_by_date = find_medical_attendance_by_date

    def execute(self,
                id_patient: int,
                left_foot_professional_observation: str,
                right_foot_professional_observation: str,
                type_pressure_left_foot: str,
                type_pressure_right_foot: str,
                left_foot_mono_filament_test: str,
                right_foot_mono_filament_test: str,
                left_foot_dermatological_pathology: str,
                right_foot_dermatological_pathology: str,
                pathology_present_in_nail_left_foot: str,
                pathology_present_in_nail_right_foot: str,
                performed_procedure: str,
                date_of_schedule: str) -> HttpResponse:
        patient = self.__patient_exists(patient_id=id_patient)
        pathology = self.__pathology_exists(patient_id=id_patient)

        date_of_scheduling = DateFormat.str_to_datetime_schedule(value=date_of_schedule)
        self.__check_medical_attendance(date_of_schedule=date_of_schedule, patient=patient)

        medical_attendance = MedicalAttendance(
            id_patient=id_patient,
            id_pathology=pathology[0]["id_pathology"],
            left_foot_professional_observation=left_foot_professional_observation,
            right_foot_professional_observation=right_foot_professional_observation,
            type_pressure_left_foot=type_pressure_left_foot,
            type_pressure_right_foot=type_pressure_right_foot,
            left_foot_mono_filament_test=left_foot_mono_filament_test,
            right_foot_mono_filament_test=right_foot_mono_filament_test,
            left_foot_dermatological_pathology=left_foot_dermatological_pathology,
            right_foot_dermatological_pathology=right_foot_dermatological_pathology,
            pathology_present_in_nail_left_foot=pathology_present_in_nail_left_foot,
            pathology_present_in_nail_right_foot=pathology_present_in_nail_right_foot,
            performed_procedure=performed_procedure,
            consultation_completed=1,
            date_consultation_completed=DateFormat.get_date_and_hour_current()
        )
        self.__create_medical_attendance.create(medical_attendance=medical_attendance, date_of_schedule=date_of_scheduling)
        return HttpResponse(status_code=200, body={"attendance": f"Atendimento do paciente {patient['first_name']} realizado."})

    def __patient_exists(self, patient_id: int):
        patient = self.__find_patient_by_id.find(id_patient=patient_id)
        if len(patient) < 1:
            raise MyCustomError(message="Paciente não econtrado", status_code=404)
        return patient

    def __pathology_exists(self, patient_id: int):
        pathology = self.__find_by_pathology_by_patient_id.find(id_patient=patient_id)
        if len(pathology) < 1:
            raise MyCustomError(message="Paciente não tem patologia registrada", status_code=400)
        return pathology

    def __check_medical_attendance(self, date_of_schedule: str, patient: dict):
        date_of_scheduling = DateFormat.str_to_datetime_schedule(value=date_of_schedule)
        medical_att = self.__find_medical_attendance_by_date.find(date_of_schedule=date_of_scheduling)
        if len(medical_att) > 0:
            if medical_att[0]["consultation_completed"] == 1:
                raise MyCustomError(message=f"Ops.. já foi feito atendimento para o paciente"
                                            f" {patient['first_name']} com essa data de agendamento"
                                            f" {date_of_schedule}.")
