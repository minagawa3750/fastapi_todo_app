from datetime import date
from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class UpdateTasksUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def update_task(self,
            db: Session,
            id: int,
            title: str,
            memo: str,
            start_date: date,
            finish_date: date,
            is_check: bool
        ):
        return self.task_repo.update_task(db, id, title, memo, start_date, finish_date, is_check)