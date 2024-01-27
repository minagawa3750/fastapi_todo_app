from datetime import date, datetime

from settings.database import Base
from typing import Optional, List
from models.user import UserOrm
from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, DateTime
from sqlalchemy.orm import relationship

class TaskOrm(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(), primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    todo = Column(String(100), nullable=False)
    is_check = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(
        DateTime(timezone=True), 
        default=datetime.now(), 
        onupdate=datetime.now()
    )

    user = relationship("UserOrm", back_populates="task")

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

class TaskCreate(BaseModel):
    todo: str

class TaskUpdate(BaseModel):
    id: int
    is_check: bool