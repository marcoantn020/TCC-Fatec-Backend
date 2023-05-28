from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class UserOutputLogin(BaseModel):
    id: int
    name: Optional[str]
    username: str
    admin: int


class LoginInput(BaseModel):
    username: str = Field("marco")
    password: str = Field("123456")


class ResponseToken(BaseModel):
    access_token: str = Field("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    user: UserOutputLogin = Field(
                        {
                            "id": 2,
                            "name": "johndoe",
                            "username": "johnDoe",
                            "admin": 0
                        })
