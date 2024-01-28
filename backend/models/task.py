from datetime import datetime

from settings.database import Base
from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class TaskOrm(Base):
    __tablename__ = 'task'
    __table_args__ = {'comment': 'タスクを管理するテーブル'} 

    id = Column(Integer(), primary_key=True, nullable=False, index=True, comment='タスクのID')
    todo = Column(String(100), nullable=False, comment='やること')
    is_check = Column(Boolean(), default=False, comment='タスク完了、未完了フラグ')
    created_at = Column(DateTime(timezone=True), default=datetime.now(), comment='作成日時')
    updated_at = Column(
        DateTime(timezone=True), 
        default=datetime.now(), 
        onupdate=datetime.now(),
        comment='更新日時'
    )

class Task(BaseModel):
    id: int
    todo: str
    is_check: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TaskList(BaseModel):
    completed_tasks: List[Task]
    incompleted_tasks: List[Task]

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    todo: str

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    id: int
    is_check: bool

    class Config:
        orm_mode = True