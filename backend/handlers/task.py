import logging

from fastapi import APIRouter, Request, Depends, HTTPException
from typing import Annotated
from repositories.task import TaskRepository
from settings.database import SessionLocal

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/new_task")
def create_task(request: Request, user_repo: Annotated[TaskRepository, Depends(TaskRepository)]):
    try:
        with SessionLocal.begin() as db:
            user_repo.create_task(db, request.user_id, request.title, request.memo, request.start_date, request.finish_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))