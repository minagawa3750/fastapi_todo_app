from fastapi import FastAPI
from handlers import task, test

app = FastAPI()

app.include_router(task.router)
app.include_router(test.router)