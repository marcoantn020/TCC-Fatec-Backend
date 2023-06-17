from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import Request
from fastapi import status

from typing import List

from src.dataProvider.service.JWTBearer import JWTBearer
from src.entrypoint.api.v1.util.GetUserDataLogged import GetUserDataLogged

from src.core.usecase.utils.Validations import Validations

from src.entrypoint.controller.patient.admin.AdminFindPatientByIdController import AdminFindPatientByIdController
from src.entrypoint.controller.patient.admin.AdminFindPatientAllController import AdminFindPatientAllController
from src.entrypoint.controller.patient.admin.AdminFindPatientByNameController import AdminFindPatientByNameController

from src.entrypoint.controller.pathology.admin.AdminCreatePathologyController import AdminCreatePathologyController

from src.entrypoint.controller.schedule.admin.AdminScheduleCancelController import AdminScheduleCancelController
from src.entrypoint.controller.schedule.admin.AdminFindScheduleByDateController import AdminFindScheduleByDateController

from src.entrypoint.controller.medical.MedicalAttendanceController import MedicalAttendanceController

from src.entrypoint.schemas.pathology_schema import PathologyInputCreate
from src.entrypoint.schemas.pathology_schema import PathologyCreate

from src.entrypoint.schemas.patient_schema import PatientOutput

from src.entrypoint.schemas.schedule_schema import ScheduleInputCancel
from src.entrypoint.schemas.schedule_schema import FindScheduleByDate
from src.entrypoint.schemas.schedule_schema import ScheduleTodayOutput

from src.entrypoint.schemas.medical_attendance_schema import InputMedicalAttendance
from src.entrypoint.schemas.medical_attendance_schema import OutputMedicalAttendance

from src.core.usecase.utils import MyCustomError


router = APIRouter()


@router.post("/register/pathology", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED,
             response_model=PathologyCreate)
def create_new_patient(request: Request, pathology: PathologyInputCreate):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        new_pathology = AdminCreatePathologyController.handle(input_data=pathology)
        return new_pathology
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get("/search/patient/{patient_id}", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
            response_model=PatientOutput)
def find_patient_by_id(request: Request, patient_id: int):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        patient = AdminFindPatientByIdController.handle(id_patient=patient_id)
        return patient
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get("/list/patient", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
            response_model=List[PatientOutput])
def find_all_patients(request: Request, limit: int = None, offset: int = None):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        list_users = AdminFindPatientAllController.handle(limit=limit, offset=offset)
        return list_users
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get("/search/patient/by/{name}", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
            response_model=PatientOutput)
def find_patient_by_name(request: Request, name: str):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        patient = AdminFindPatientByNameController.handle(name=name)
        return patient
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.post("/schedule/cancel", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
def cancel_schedule(request: Request, schedule_cancel: ScheduleInputCancel):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        patient = AdminScheduleCancelController.handle(input_data=schedule_cancel)
        return patient
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.post("/schedule/list", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
            #  response_model=List[ScheduleTodayOutput])
def find_schedule_by_date(request: Request, date: FindScheduleByDate):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        scheduling = AdminFindScheduleByDateController.handle(input_data=date)
        return scheduling
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.post("/medical_attendance", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
             response_model=OutputMedicalAttendance)
def medical_attendance(request: Request, attendance: InputMedicalAttendance):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        Validations.user_is_admin(is_admin)
        scheduling = MedicalAttendanceController.handle(input_data=attendance)
        return scheduling
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)
