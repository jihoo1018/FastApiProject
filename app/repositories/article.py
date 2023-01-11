import pymysql
from sqlalchemy.orm import Session
from app.models.article import Article
from app.database import conn

pymysql.install_as_MySQLdb()

def find_article_legacy():
    cursor = conn.cursor()
    sql = "select * from article"
    cursor.execute(sql)
    return cursor.fetchall()


def find_articles(page:int,db: Session):
    print(f"page number is {page}")
    return db.query(Article).all()

def join(item, db):
    return None


def login(id, item, db):
    return None


def update(id, item, db):
    return None


def delte(id, item, db):
    return None


def find_article(id, db):
    return None


def find_articles_by_job(search, page, db):
    return None


def find_article_by_title(search, page, db):
    return None