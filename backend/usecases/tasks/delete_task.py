from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class DeleteTaskUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def delete_task(self, db: Session, id: int):
        self.task_repo.delete_task(db, id)