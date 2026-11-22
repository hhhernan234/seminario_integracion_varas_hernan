from fastapi import FastAPI
from routers.hello_word_mp_varas_hernan import router
from routers.tasks_router_mp_varas_hernan import expedientes_router

app = FastAPI(title="Expedientes Policiales - Hernan Varas")
app.include_router(router)
app.include_router(expedientes_router)
