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
    def add_article(self, request_article: ArticleDTO) -> str:
        self.db.add(Article(**request_article.dict()))
        self.db.commit()
        return "success"

    def update_article(self, request_article: ArticleDTO) -> str:
        pass

    def delete_article(self, request_article: ArticleDTO) -> str:
        self.find_article_by_seq(Article.art_seq)
        self.db.query(Article).delete()

    def find_all_articles(self, page: int, db:Session) -> List[Article]:
        return self.db.query(Article).all()

    def find_articles_by_user_id(self, user_id:str) -> ArticleDTO:
        pass

    def find_articles_by_title(self, title:str) ->  List[ArticleDTO]:
        pass

    def find_article_by_seq(self, request_article: ArticleDTO) -> ArticleDTO:
        article = Article(**request_article.dict())
        return self.db.query(User).filter(Article.art_seq == article.art_seq).first()
