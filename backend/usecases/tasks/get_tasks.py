from repositories.task import TaskRepository
from fastapi import Depends
from sqlalchemy.orm import Session

class GetTasksUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def get_tasks(self, db: Session):
        return self.task_repo.get_tasks(db)