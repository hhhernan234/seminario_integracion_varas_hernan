from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_word import router
from routers.tasks_router import tasks_router

app = FastAPI(title="Curso FastAPI + uv")
app.include_router(router)
app.include_router(tasks_router)
