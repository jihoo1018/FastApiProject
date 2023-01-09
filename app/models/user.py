from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'blogusers'
    blog_userid = Column(primary_key=True)
    email = Column(String(20), nullable=False)
    nickname = Column(String(20))
    password = Column(String(20),nullable=False)

    class Config:
        arbitrary_types_allowed = True
