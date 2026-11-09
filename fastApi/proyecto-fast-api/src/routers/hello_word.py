from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv",
            "autor": "Ing.Roberto Rocha",
            "version": "0.1.0"}

@router.get("/roberto")
def endpoint_roberto() -> Mensaje:
    return {"texto" : "Hola", 
            "campo_interno" : "imprime desde endpoint higuera"}


@router.get("/rocha", response_model=Mensaje)
def endpoint_rocha():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "no debería salir"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Roberto", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra" : "no debe salir esto"}