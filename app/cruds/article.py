from abc import ABC
from typing import List

import pymysql
from sqlalchemy.orm import Session

from app.bases.article import ArticleBase
from app.bases.user import UserBase
from app.models.article import Article
from app.models.user import User
from app.schemas.article import ArticleDTO
from app.schemas.user import UserDTO

pymysql.install_as_MySQLdb()

class ArticleCrud(ArticleBase,ABC):
    def __init__(self, db: Session):
        self.db: Session = db
    def write(self, request_article: ArticleDTO) -> str:
        print(f"###1###{request_article}")
        self.db.add(Article(**request_article.dict()))
        print(f"###2###{request_article}")
        self.db.commit()
        return "success"

    def update_article(self, request_article: ArticleDTO) -> str:
        pass

    def delete_article(self, request_article: ArticleDTO) -> str:
        pass

    def find_all_articles(self, page: int, db:Session) -> List[Article]:
        print(f" page number is {page}")
        return self.db.query(Article).all()

    def find_articles_by_user_id(self, request_article: ArticleDTO) -> ArticleDTO:
        pass

    def find_articles_by_title(self, request_article: ArticleDTO) -> str:
        pass