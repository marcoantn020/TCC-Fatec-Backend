from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from src.entrypoint.controller.login.LoginController import LoginController
from src.entrypoint.schemas.login_schema import LoginInput
from src.entrypoint.schemas.login_schema import ResponseToken

from src.core.usecase.utils import MyCustomError

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK, response_model=ResponseToken)
def login(user: LoginInput):
    try:
        login_generate = LoginController.handle(user)
        return login_generate
    except MyCustomError as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)
