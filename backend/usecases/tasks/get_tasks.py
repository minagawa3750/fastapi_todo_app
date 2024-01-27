from repositories.task import TaskRepository
from models.task import TaskList
from fastapi import Depends
from sqlalchemy.orm import Session

class GetTasksUsecase:
    def  __init__(self, task_repo: TaskRepository = Depends(TaskRepository)):
        self.task_repo = task_repo
    
    def get_tasks(self, db: Session):
        tasks = self.task_repo.get_tasks(db)
        completed_tasks, incompleted_tasks = self.split_tasks(tasks)
        return {"completed_tasks": completed_tasks, "incompleted_tasks": incompleted_tasks}

    def split_tasks(self, tasks) -> TaskList:
        completed_tasks = []
        incompleted_tasks = []

        for task in tasks:
            if task.is_check:
                completed_tasks.append(task)
            else:
                incompleted_tasks.append(task)

        return completed_tasks, incompleted_tasks