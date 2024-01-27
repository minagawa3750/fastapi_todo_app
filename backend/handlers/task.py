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

@router.post("/new_task", summary="タスクの新規作成", tags=['task'])
def create_task(task: TaskCreate, task_usecase: CreateTaskUsecase = Depends(CreateTaskUsecase)):
    try:
        with SessionLocal.begin() as db:
            task_usecase.create_task(db, task.todo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tasks", summary="タスクの一覧取得", tags=['task'])
def get_tasks(task_usecase: GetTasksUsecase = Depends(GetTasksUsecase)):
    try:
        with SessionLocal() as db:
            return task_usecase.get_tasks(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/task/{id}", summary="タスクの詳細取得", response_model=Task, tags=['task'])
def get_task(id: int, task_usecase: GetTaskDetailsUsecase = Depends(GetTaskDetailsUsecase)):
    try:
        with SessionLocal() as db:
            return task_usecase.get_task_details(db, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/task/{id}", summary="タスクの更新処理", tags=['task'])
def update_task(task: TaskUpdate, task_usecase: UpdateTasksUsecase = Depends(UpdateTasksUsecase)):
    try:
        with SessionLocal.begin() as db:
            tasks = task_usecase.update_task(db, task.id, task.is_check)
            print(f"なんでとおらないんだよぉぉぉぉぉおぉっぉぉｘ{tasks}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/task/{id}", summary="タスクの削除処理", tags=['task'])
def delete_task(id: int, task_usecase: DeleteTaskUsecase = Depends(DeleteTaskUsecase)):
    try:
        with SessionLocal.begin() as db:
            task_usecase.delete_task(db, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))