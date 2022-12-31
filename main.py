from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.entrypoint.api.v1.api_v1 import api_router
from src.config.config import config


app: FastAPI = FastAPI(
    title="API para consultorio de podologos",
    description="Api desenvolvida para facilitar o dia dos podologos, gerenciando sua agenda e atendimentos.Projeto de Conclusao de Curso"
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config["versions"]["API_V1"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info", reload=True)
