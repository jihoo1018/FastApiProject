from abc import abstractmethod, ABCMeta
from typing import List
from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def write(self, request_article:ArticleDTO)-> str: pass

    @abstractmethod
    def update_article(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def delete_article(self, request_article: ArticleDTO) -> str: pass

    @abstractmethod
    def find_all_articles(self, page: int, db:Session) -> List[Article]: pass

    @abstractmethod
    def find_articles_by_user_id(self, request_article: ArticleDTO) -> ArticleDTO: pass

    @abstractmethod
    def find_articles_by_title(self, request_article: ArticleDTO) -> str: pass