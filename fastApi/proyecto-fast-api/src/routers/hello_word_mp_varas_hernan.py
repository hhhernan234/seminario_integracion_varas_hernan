from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class ExpedienteInterno(BaseModel):
    descripcion: str
    prioridad: int = 1
    campo_interno: str


class ExpedientePublico(BaseModel):
    descripcion: str
    prioridad: int = 1


@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv - Sistema de Expedientes Policiales",
            "autor": "Inspector Hernan Varas",
            "version": "0.1.0"}


@router.get("/hernan")
def endpoint_hernan() -> ExpedienteInterno:
    return ExpedienteInterno(descripcion="Robo agravado EXP-2026-001",
                             campo_interno="imprime desde endpoint de Hernan Varas")


@router.get("/expediente", response_model=ExpedientePublico)
def endpoint_expediente():
    # response_model filtra: campo_interno NO sale en la respuesta
    return {"descripcion": "Homicidio EXP-2026-002",
            "prioridad": 5,
            "campo_interno": "no debería salir"}


@router.get("/campo-extra", response_model=ExpedienteInterno)
def endpoint_campo_extra():
    # response_model filtra: campo_extra NO sale, campo_interno sí
    return {"descripcion": "Secuestro EXP-2026-003",
            "prioridad": 5,
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no debe salir esto"}
