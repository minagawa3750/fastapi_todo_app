from datetime import date
from sqlalchemy.orm import Session
from models.task import TaskOrm, Task
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    memo: str
    start_date: date
    finish_date: date

class TaskUpdate(BaseModel):
    id: int
    title: str
    memo: str
    start_date: date
    finish_date: date
    is_check: bool

class TaskRepository:
    # タスクの新規作成
    def create_task(
            self, 
            db: Session, 
            title: str, 
            memo: str, 
            start_date: date, 
            finish_date: date
        ) -> TaskCreate:
        task = TaskOrm (
            title = title,
            memo = memo,
            start_date = start_date,
            finish_date = finish_date
        )
        db.add(task)
        db.flush()

        return task

    # タスクの一覧取得
    def get_tasks(self, db: Session) -> Task:
        return db.query(TaskOrm).all()
    
    # タスクの詳細取得
    def get_task_by_id(self, db: Session, id: int):
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
        ) -> TaskUpdate:

        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()

        if task is None:
            raise ValueError("Task is None")

        task.title = title
        task.memo = memo
        task.start_date = start_date
        task.finish_date = finish_date
        task.is_check = is_check

        db.flush()

        return task

    # タスクの削除処理
    def delete_task(self, db: Session, id: int):
        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()

        if task:
            db.delete(task)
            db.flush
        else:
            raise ValueError("Task is None")