import logging

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from models.task import Task
from repositories.task import TaskRepository
from settings.database import SessionLocal

router = APIRouter()
logger = logging.getLogger(__name__)

# タスクの新規作成
@router.post("/new_task")
def create_task(task: Task, user_repo: Annotated[TaskRepository, Depends(TaskRepository)]):
    try:
        with SessionLocal.begin() as db:
            user_repo.create_task(db, task.title, task.memo, task.start_date, task.finish_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))