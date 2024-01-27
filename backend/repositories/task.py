from datetime import date
from sqlalchemy.orm import Session
from models.task import TaskOrm, Task, TaskCreate, TaskUpdate

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