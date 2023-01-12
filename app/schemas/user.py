from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from app.schemas.article import Article


class User(BaseModel):
    user_id : Optional[UUID]
    email : str
    nickname : str
    password : str
    create_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserDetail(User):
    articles: List[Article] = []