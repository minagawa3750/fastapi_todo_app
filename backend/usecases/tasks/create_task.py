from datetime import date
from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class CreateTaskUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def create_task(self, db: Session, todo: str):
        self.task_repo.create_task(db, todo)
