from fastapi import APIRouter

from src.entrypoint.api.v1.routes import patient_route
from src.entrypoint.api.v1.routes import login_route
from src.entrypoint.api.v1.routes import podiatrist_route

api_router: APIRouter = APIRouter()

api_router.include_router(login_route.router, prefix="/login", tags=["Login"])
api_router.include_router(patient_route.router, prefix="/patient", tags=["Patient"])
api_router.include_router(podiatrist_route.router, prefix="/podiatrist", tags=["Podiatrist"])

