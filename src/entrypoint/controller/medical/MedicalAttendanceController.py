from src.entrypoint.schemas.medical_attendance_schema import InputMedicalAttendance
from src.core.usecase.medical.impl.MedicalAttendanceUseCaseImpl import MedicalAttendanceUseCaseImpl
from src.dataProvider.repositories.medical.CreateMedicalAttendanceImpl import CreateMedicalAttendanceImpl
from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.dataProvider.repositories.pathology.FindByPathologyByPatientIdImpl import FindByPathologyByPatientIdImpl
from src.dataProvider.repositories.medical.FindMedicalAttendanceByDateImpl import FindMedicalAttendanceByDateImpl


class MedicalAttendanceController:

    @staticmethod
    def handle(input_data: InputMedicalAttendance):
        create_medical_attendance = CreateMedicalAttendanceImpl()
        find_patient_by_id = FindPatientByIdImpl()
        find_by_pathology_by_patient_id = FindByPathologyByPatientIdImpl()
        find_medical_attendance_by_date = FindMedicalAttendanceByDateImpl()
        medical_attendance_use_case = MedicalAttendanceUseCaseImpl(
            create_medical_attendance=create_medical_attendance,
            find_patient_by_id=find_patient_by_id,
            find_by_pathology_by_patient_id=find_by_pathology_by_patient_id,
            find_medical_attendance_by_date=find_medical_attendance_by_date
        )
        return medical_attendance_use_case.execute(
            id_patient=input_data.id_patient,
            left_foot_professional_observation=input_data.left_foot_professional_observation,
            right_foot_professional_observation=input_data.right_foot_professional_observation,
            type_pressure_left_foot=input_data.type_pressure_left_foot,
            type_pressure_right_foot=input_data.type_pressure_right_foot,
            left_foot_mono_filament_test=input_data.left_foot_mono_filament_test,
            right_foot_mono_filament_test=input_data.right_foot_mono_filament_test,
            left_foot_dermatological_pathology=input_data.left_foot_dermatological_pathology,
            right_foot_dermatological_pathology=input_data.right_foot_dermatological_pathology,
            pathology_present_in_nail_left_foot=input_data.pathology_present_in_nail_left_foot,
            pathology_present_in_nail_right_foot=input_data.pathology_present_in_nail_right_foot,
            performed_procedure=input_data.performed_procedure,
            date_of_schedule=input_data.date_of_scheduling
        )
