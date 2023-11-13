import datetime

from settings.database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime


class UserOrm(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False)

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True