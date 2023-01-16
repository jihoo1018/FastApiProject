from abc import ABC
from typing import List

import pymysql
from sqlalchemy.orm import Session

from app.bases.user import UserBase
from app.models.article import Article
from app.database import conn
from app.schemas.article import ArticleDTO

pymysql.install_as_MySQLdb()

class ArticleCrud(UserBase,ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: ArticleDTO) -> str:
        print(f"###1###{request_article}")
        self.db.add(Article(**request_article.dict()))
        print(f"###2###{request_article}")
        self.db.commit()
        return "success"

    def login(self, request_article: ArticleDTO) -> Article:
        pass



    def update_user(self, request_article: ArticleDTO) -> str:
        pass

    def delete_user(self, request_article: ArticleDTO) -> str:
        pass

    def find_all_users(self, page: int) -> List[Article]:
        pass

    def find_user_by_id(self, request_article: ArticleDTO) -> ArticleDTO:
        pass
    def find_user_by_email(self, request_article: ArticleDTO) -> str:
       pass