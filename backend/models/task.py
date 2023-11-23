from datetime import date, datetime

from settings.database import Base
from typing import Optional
from models.user import UserOrm
from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, DateTime
from sqlalchemy.orm import relationship

class TaskOrm(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(), primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    title = Column(String(100), nullable=False)
    memo = Column(Text(1000), nullable=True)
    start_date = Column(Date(), nullable=False)
    finish_date = Column(Date(), nullable=False)
    is_check = Column(Boolean(), default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(
        DateTime(timezone=True), 
        default=datetime.now(), 
        onupdate=datetime.now()
    )

    user = relationship("UserOrm", back_populates="task")

class Task(BaseModel):
    id: int
    title: str
    memo: Optional[str]
    start_date: date
    finish_date: date
    is_check: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True