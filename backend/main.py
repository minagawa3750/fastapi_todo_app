from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings.env import Env
from handlers import task

app = FastAPI()

origins = [
    Env.APP_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task.router)