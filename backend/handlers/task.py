import logging

from fastapi import APIRouter, Depends, HTTPException
from models.task import Task
from repositories.task import TaskCreate, TaskUpdate
from usecases.tasks.create_task import CreateTaskUsecase
from usecases.tasks.get_tasks import GetTasksUsecase
from usecases.tasks.get_task_details import GetTaskDetailsUsecase
from usecases.tasks.update_task import UpdateTasksUsecase
from usecases.tasks.delete_task import DeleteTaskUsecase
from settings.database import SessionLocal

router = APIRouter()
logger = logging.getLogger(__name__)

# タスクの新規作成
@router.post("/new_task")
def create_task(task: TaskCreate, task_usecase: CreateTaskUsecase = Depends(CreateTaskUsecase)):
    try:
        with SessionLocal.begin() as db:
            task_usecase.create_task(db, task.todo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの一覧取得
@router.get("/tasks")
def get_tasks(task_usecase: GetTasksUsecase = Depends(GetTasksUsecase)):
    try:
        with SessionLocal() as db:
            return task_usecase.get_tasks(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの詳細取得
@router.get("/task/{id}", response_model=Task)
def get_task(id: int, task_usecase: GetTaskDetailsUsecase = Depends(GetTaskDetailsUsecase)):
    try:
        with SessionLocal() as db:
            return task_usecase.get_task_details(db, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの更新処理
@router.put("/task/{id}")
def update_task(task: TaskUpdate, task_usecase: UpdateTasksUsecase = Depends(UpdateTasksUsecase)):
    try:
        with SessionLocal.begin() as db:
            task_usecase.update_task(db, task.id, task.is_check)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# タスクの削除処理
@router.delete("/task/{id}")
def delete_task(id: int, task_usecase: DeleteTaskUsecase = Depends(DeleteTaskUsecase)):
    try:
        with SessionLocal.begin() as db:
            task_usecase.delete_task(db, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))