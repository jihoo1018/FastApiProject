from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app.database import Base
from app.models.mixins import TimestampMixin


class Article(Base, TimestampMixin):
    __tablename__ = 'article'
    art_seq = Column(Integer, primary_key=True, auto_increment=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = Column(UUIDType(binary=False),ForeignKey('blogusers.user_id'),nullable=False)

    user = relationship('User', back_populates='articles')

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True
