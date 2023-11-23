from datetime import date
from sqlalchemy.orm import Session
from models.task import TaskOrm, Task

class TaskRepository:
    # タスクの新規作成
    def create_task(
            self, 
            db: Session, 
            title: str, 
            memo: str, 
            start_date: date, 
            finish_date: date
        ) -> Task:
        task = TaskOrm (
            title = title,
            memo = memo,
            start_date = start_date,
            finish_date = finish_date
        )
        db.add(task)
        db.flush()
