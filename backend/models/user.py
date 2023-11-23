import datetime

from settings.database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class UserOrm(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = Column(
        DateTime(timezone=True), 
        default=datetime.datetime.now(), 
        onupdate=datetime.datetime.now()
    )

    task = relationship("TaskOrm", back_populates="user")

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True