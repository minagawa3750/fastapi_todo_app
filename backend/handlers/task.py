import logging

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from models.task import Task
from repositories.task import TaskRepository, TaskCreate, TaskUpdate
from settings.database import SessionLocal

router = APIRouter()
logger = logging.getLogger(__name__)

# タスクの新規作成
@router.post("/new_task")
def create_task(task: TaskCreate, task_repo: Annotated[TaskRepository, Depends(TaskRepository)]):
    try:
        with SessionLocal.begin() as db:
            task_repo.create_task(db, task.title, task.memo, task.start_date, task.finish_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの詳細取得
@router.get("/task/{id}", response_model=Task)
def get_task(id: int, task_repo: Annotated[TaskRepository, Depends(TaskRepository)]):
    try:
        with SessionLocal() as db:
            return task_repo.get_task_by_id(db, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの更新処理
@router.put("/task/{id}")
def update_task(task: TaskUpdate, task_repo: Annotated[TaskRepository, Depends(TaskRepository)]):
    try:
        with SessionLocal.begin() as db:
            task_repo.update_task(db, task.id, task.title, task.memo, 
                                    task.start_date, task.finish_date, task.is_check)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))