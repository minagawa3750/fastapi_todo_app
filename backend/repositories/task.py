from datetime import date
from sqlalchemy.orm import Session
from models.task import TaskOrm, Task
from pydantic import BaseModel

class TaskCreate(BaseModel):
    todo: str

class TaskUpdate(BaseModel):
    id: int
    is_check: bool

class TaskRepository:
    # タスクの新規作成
    def create_task(
            self, 
            db: Session, 
            todo: str, 
        ) -> TaskCreate:
        task = TaskOrm (
            todo = todo,
        )
        db.add(task)
        db.flush()

        return task

    # タスクの一覧取得
    def get_tasks(self, db: Session) -> Task:
        return db.query(TaskOrm).all()
    
    # 未完了タスクの一覧取得
    def get_incomplete_tasks(self, db: Session) -> Task:
        incomplete_tasks = db.query(TaskOrm).filter(TaskOrm.is_check == 0).all()
        if incomplete_tasks is None:
            raise ValueError("incomplete_tasks is None")
        
        return incomplete_tasks
    
    # 完了タスクの一覧取得
    def get_complete_tasks(self, db: Session) -> Task:
        complete_tasks = db.query(TaskOrm).filter(TaskOrm.is_check == 1).all()
        if complete_tasks is None:
            raise ValueError("complete_tasks is None")
        
        return complete_tasks
    
    # タスクの詳細取得
    def get_task_details(self, db: Session, id: int):
        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()
        if task is None:
            raise ValueError("Task is None")
        
        return task

    # タスクの更新処理
    def update_task(
            self,
            db: Session,
            id: int,
            is_check: bool
        ) -> TaskUpdate:

        task = db.query(TaskOrm).filter(TaskOrm.id == id).first()

        if task is None:
            raise ValueError("Task is None")

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