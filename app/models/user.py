from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from app.database import Base
from app.models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'blogusers'
    user_id = Column(UUIDType(binary=False),primary_key=True)
    email = Column(String(20), nullable=False)
    nickname = Column(String(20), nullable=False)
    password = Column(String(20),nullable=False)

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True
