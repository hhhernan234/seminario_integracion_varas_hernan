# routers/tasks_router_mp_varas_hernan.py — CRUD de expedientes policiales
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

expedientes_router = APIRouter()


class ExpedienteCreate(BaseModel):
    """Lo que el cliente envía para crear un expediente. Sin id: lo asigna el servidor."""
    titulo: str = Field(min_length=3, max_length=100)
    descripcion: str | None = None
    prioridad: str = "media"
    etiquetas: list[str] = Field(default_factory=list)
    inspector: str = "Hernan Varas"


class ExpedienteRead(BaseModel):
    """Lo que el servidor expone al leer un expediente. Incluye campos calculados por el servidor."""
    id: int
    titulo: str
    descripcion: str | None
    prioridad: str
    etiquetas: list[str]
    inspector: str
    esta_cerrado: bool


class ExpedienteUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    descripcion: str | None = None
    prioridad: str | None = None
    etiquetas: list[str] | None = None
    inspector: str | None = None
    esta_cerrado: bool | None = None


EXPEDIENTES: list[dict] = [
    {"id": 1, "titulo": "Robo agravado Banco Central", "descripcion": None, "prioridad": "alta",
     "etiquetas": ["robo", "fiscalia"], "inspector": "Hernan Varas", "esta_cerrado": False},
    {"id": 2, "titulo": "Fraude bancario", "descripcion": None, "prioridad": "media",
     "etiquetas": ["fraude", "delitos-economicos"], "inspector": "Hernan Varas", "esta_cerrado": False},
]
NEXT_ID = len(EXPEDIENTES) + 1


@expedientes_router.post("/expedientes", response_model=ExpedienteRead)
def crear_expediente(expediente: ExpedienteCreate) -> dict:
    global NEXT_ID
    nuevo = {
        "id": NEXT_ID,
        "esta_cerrado": False,
        "notas_internas": "creado desde la API",  # campo interno, nunca debería salir al cliente
        **expediente.model_dump(),
    }
    EXPEDIENTES.append(nuevo)
    NEXT_ID += 1
    return nuevo


@expedientes_router.get("/expedientes", response_model=list[ExpedienteRead])
def listar_expedientes() -> list[dict]:
    return EXPEDIENTES


@expedientes_router.patch("/expedientes/{expediente_id}", response_model=ExpedienteRead)
def actualizar_expediente(expediente_id: int, cambios: ExpedienteUpdate) -> dict:
    for expediente in EXPEDIENTES:
        if expediente["id"] == expediente_id:
            expediente.update(cambios.model_dump(exclude_unset=True))
            return expediente
    raise HTTPException(status_code=404, detail="Expediente no encontrado")


@expedientes_router.post("/expedientes/from-model")
def crear_desde_modelo(expediente: ExpedienteCreate) -> dict:
    global NEXT_ID
    # model_dump(): instancia de Pydantic -> dict plano de Python
    datos = expediente.model_dump()
    nuevo = {"id": NEXT_ID, "esta_cerrado": False, **datos}
    EXPEDIENTES.append(nuevo)
    NEXT_ID += 1

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validado = ExpedienteRead.model_validate(nuevo)
    return validado.model_dump()


@expedientes_router.get("/expedientes/{expediente_id}/raw-vs-validated")
def comparar_raw_validado(expediente_id: int) -> dict:
    raw = next((e for e in EXPEDIENTES if e["id"] == expediente_id), None)
    if raw is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")

    # model_validate lanza una excepción si el dict no cumple el schema de ExpedienteRead
    validado = ExpedienteRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validado.model_dump(),
        "validated_model_dump_json": validado.model_dump_json(),
    }


@expedientes_router.delete("/expedientes/{expediente_id}")
def eliminar_expediente(expediente_id: int) -> dict:
    for indice, expediente in enumerate(EXPEDIENTES):
        if expediente["id"] == expediente_id:
            eliminado = EXPEDIENTES.pop(indice)
            return {
                "message": "Expediente eliminado correctamente",
                "deleted_expediente": eliminado,
            }

    raise HTTPException(status_code=404, detail="Expediente no encontrado")


@expedientes_router.get("/expedientes/{expediente_id}", response_model=ExpedienteRead)
def obtener_expediente(expediente_id: int) -> dict:
    for expediente in EXPEDIENTES:
        if expediente["id"] == expediente_id:
            return expediente
    # El raise va FUERA del for: si estuviera dentro, solo funcionaría el primer expediente
    raise HTTPException(status_code=404, detail="Expediente no encontrado")
