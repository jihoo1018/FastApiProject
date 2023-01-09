from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(BigInteger,String(20),auto_increment=True,primary_key=True)
    title = Column(String(100))
    content = Column(String(1000))
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Config:
        arbitrary_types_allowed = True
