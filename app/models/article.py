from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy_utils import UUIDType

from app.models.mixins import TimestampMixin


class Article(Base,TimestampMixin):

    __tablename__ = 'article'

    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='article')


    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def __str__(self):
        return f'글쓴이: {self.user_id}, \n ' \
               f'글번호: {self.art_seq}, \n ' \
               f'제목: {self.title} \n ' \
               f'내용: {self.content} \n ' \
               f'작성일: {self.created} \n' \
               f'수정일: {self.modified} \n'