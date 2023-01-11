from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel
from app.schemas.article import Article


class User(BaseModel):
    user_id : UUID
    email : str
    nickname : str
    password : str
    create_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserDetail(User):
    articles: List[Article] = []