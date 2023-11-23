from fastapi import FastAPI
from handlers import task

app = FastAPI()

app.include_router(task.router)