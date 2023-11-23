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
    
    # タスクの詳細取得
    def get_task_by_id(self, db: Session, id: int) -> Task:
        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()
        if task is None:
            raise ValueError("Task is None")
        
        return task

    # タスクの更新処理
    def update_task(
            self,
            db: Session,
            id: int,
            title: str,
            memo: str,
            start_date: date,
            finish_date: date,
            is_check: bool
        ) -> Task:

        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()

        if task is None:
            raise ValueError("Task is None")

        task.title = title,
        task.memo = memo,
        task.start_date = start_date,
        task.finish_date = finish_date,
        task.is_check = is_check

        db.flush()