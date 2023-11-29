from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class GetTaskDetailsUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def get_task_details(self, db: Session, id: int):
        return self.task_repo.get_task_details(db, id)
        