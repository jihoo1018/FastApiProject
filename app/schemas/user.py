
from typing import List, Optional
from pydantic import BaseModel
from app.schemas.article import Article


class UserDTO(BaseModel):
    user_id : Optional[str]
    email : Optional[str]
    password : Optional[str]
    nickname : Optional[str]
    create_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

class UserDetail(UserDTO):
    articles: List[Article] = []
