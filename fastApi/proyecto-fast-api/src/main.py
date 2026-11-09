from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_word import router

app = FastAPI(title="Curso FastAPI + uv")
app.include_router(router)
