from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import Request
from fastapi import status

from typing import List

from src.dataProvider.service.JWTBearer import JWTBearer
from src.entrypoint.api.v1.util.GetUserDataLogged import GetUserDataLogged

from src.entrypoint.controller.patient.CreatePatientController import CreatePatientController
from src.entrypoint.controller.patient.UpdatePatientController import UpdatePatientController
from src.entrypoint.controller.patient.FindPatientByIdController import FindPatientByIdController
from src.entrypoint.controller.schedule.ScheduleController import ScheduleController
from src.entrypoint.controller.schedule.admin.AdminFindScheduleByPatientIdController import AdminFindScheduleByPatientIdController

from src.entrypoint.schemas.patient_schema import PatientCreated
from src.entrypoint.schemas.patient_schema import PatientInputCreate
from src.entrypoint.schemas.patient_schema import PatientInputUpdate
from src.entrypoint.schemas.patient_schema import PatientOutput
from src.entrypoint.schemas.schedule_schema import ScheduleInput
from src.entrypoint.schemas.schedule_schema import ScheduleOutput
from src.entrypoint.schemas.schedule_schema import DateOfScheduling


from src.core.usecase.utils import MyCustomError


router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=PatientCreated)
def create_new_patient(user: PatientInputCreate):
    try:
        new_patient = CreatePatientController.handle(user)
        return new_patient.body
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.put("/update", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(JWTBearer())])
def update_patient(patient: PatientInputUpdate, request: Request):
    try:
        id_patient = GetUserDataLogged.get_id(request=request)
        patient_up = UpdatePatientController.handle(input_data=patient, id_patient=id_patient)
        return patient_up.body
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get("/logged", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
            response_model=PatientOutput)
def get_patient_logged(request: Request):
    try:
        is_admin: int = GetUserDataLogged.get_user_is_admin(request=request)
        patient_id: int = GetUserDataLogged.get_id(request=request)
        user_patient = FindPatientByIdController.handle(is_admin=is_admin, id_patient=patient_id)
        return user_patient.body
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.post("/schedule", dependencies=[Depends(JWTBearer())],
             status_code=status.HTTP_201_CREATED, response_model=ScheduleOutput)
def schedule(schedule_input: ScheduleInput, request: Request):
    try:
        patient_id: int = GetUserDataLogged.get_id(request=request)
        schedule_result = ScheduleController.handle(schedule=schedule_input, patient_id=patient_id)
        return schedule_result.body
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get("/schedule/list", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK,
            response_model=List[DateOfScheduling])
def schedule_list_appointment(request: Request, finish: int = 0):
    try:
        patient_id: int = GetUserDataLogged.get_id(request=request)
        schedule_result = AdminFindScheduleByPatientIdController.handle(id_patient=patient_id, finish=finish)
        return schedule_result.body
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)
