from datetime import date, datetime

from settings.database import Base
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, DateTime

class TaskOrm(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("user.id", name="task_user_id_fkey", nullable=True, ondelete="CASCADE"))
    title = Column(String(100), nullable=False)
    memo = Column(Text(1000), nullable=True)
    start_date = Column(Date, nullable=False)
    finish_date = Column(Date, nullable=False)
    is_check = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)

class Task(BaseModel):
    id: int
    user_id: Optional[int]
    title: str
    memo: Optional[str]
    start_date: date
    finish_date: date
    is_check: bool

    class Config:
        orm_mode = True