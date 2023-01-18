from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.admin.security import myuuid
from app.database import Base
from app.models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    user_id = Column(String(30),primary_key=True, default=myuuid())
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(100),nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(100))
    job = Column(String(20))
    interests = Column(String(100))
    token = Column(String(256))

    article = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'아이디: {self.user_id}, \n ' \
               f'이름: {self.username}, \n ' \
               f'이메일: {self.email} \n ' \
               f'비번: {self.password} \n' \
               f'전화번호: {self.phone} \n' \
               f'생년월일: {self.birth} \n' \
               f'주소: {self.address} \n' \
               f'직업: {self.job} \n' \
               f'관심사: {self.interests} \n' \
               f'토큰: {self.token} \n' \
               f'작성일: {self.created} \n' \
               f'수정일: {self.modified}'
