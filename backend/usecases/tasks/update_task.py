from datetime import date
from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class UpdateTasksUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def update_task(self, db: Session, id: int, is_check: bool):
        return self.task_repo.update_task(db, id, is_check)