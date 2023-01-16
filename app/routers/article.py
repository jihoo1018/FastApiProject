from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.admin.utils import current_time
from app.database import get_db
from app.cruds.article import ArticleCrud
from app.schemas.article import ArticleDTO

router = APIRouter()

@router.post("/write", status_code=201)
async def register_user(dto: ArticleDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {current_time()} ")
    print(f"Article Inform : {dto}")
    article_crud = ArticleCrud(db)
    result = article_crud.add_article(request_article=dto)
    return {"data":result}