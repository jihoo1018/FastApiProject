from app.database import conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from blogusers"
    cursor.execute(sql)
    return cursor.fetchall()

def find_users(page:int,db: Session):
    print(f"page number is {page}")
    return db.query(User).all()


def login(id:str, item:User, db:Session):
    return None


def join(item:User, db:Session):
    return None


def update(id, item, db):
    return None


def delete(id, item, db):
    return None


def find_user(id, db):
    return None


def get_users_by_nickname(search, page, db):
    return None