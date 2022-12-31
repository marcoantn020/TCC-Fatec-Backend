from fastapi import Request
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from src.dataProvider.service.JWTTokenGenerated import JWTTokenGenerated


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        is_valid_token = self.verify_jwt(credentials.credentials)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Token invalido ou expirado")

            if not is_valid_token["is_token_valid"]:
                raise HTTPException(status_code=401, detail="Token invalido ou expirado")

            return credentials.credentials
        else:
            raise HTTPException(status_code=401, detail="Token invalido ou expirado")

    @staticmethod
    def verify_jwt(jwt_token: str):
        payload = JWTTokenGenerated().decode_jwt(token=jwt_token)
        if payload:
            return {"is_token_valid": True, "data": payload}
        return {"is_token_valid": None, "data": None}

    @staticmethod
    def get_id_user_logged(request: Request):
        _, token = request.headers.get("authorization").split(" ")
        user = JWTBearer().verify_jwt(token)
        return user["data"]
