from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.admin.utils import current_time
from app.database import get_db
from app.cruds.article import ArticleCrud
from app.schemas.article import ArticleDTO

router = APIRouter()

@router.post("/write", status_code=201)
async def write(dto: ArticleDTO, db: Session = Depends(get_db)):
    print(f" 글쓰기에 진입한 시간: {current_time()} ")
    print(f"Article Inform : {dto}")
    article_crud = ArticleCrud(db)
    result = article_crud.write(request_article=dto)
    return {"data":result}

@router.get("/page/{page}")
async def get_users(page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    ls = article_crud.find_all_articles(page,db)
    return {"data": ls}