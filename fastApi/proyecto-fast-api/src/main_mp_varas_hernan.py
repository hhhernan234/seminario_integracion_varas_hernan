from fastapi import FastAPI
from routers.hello_word_mp_varas_hernan import router

app = FastAPI(title="Expedientes Policiales - Hernan Varas")
app.include_router(router)
