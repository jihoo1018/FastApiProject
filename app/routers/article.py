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
    result = article_crud.add_article(request_article=dto)
    return {"data":result}
@router.put("/modify", status_code=201)
async def modify_article(dto:ArticleDTO, db:Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.update_article(request_article=dto)
@router.delete("/remove", status_code=201)
async def remove_article(dto:ArticleDTO, db:Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.delete_article(request_article=dto)

@router.get("/page/{page}", status_code=201)
async def get_articles(page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    ls = article_crud.find_all_articles(page,db)
    return {"data": ls}

'''@router.get("/seq/{seq}", status_code=201)
async def get_articles_by_seq(art_seq:int, db:Session = Depends(get_db())):
    article_crud = ArticleCrud(db)
    article_crud.find_article_by_seq(art_seq=art_seq)'''

@router.get("/id/{user_id}/page/{page}", status_code=201)
async def get_articles_by_user_id(user_id:str,page:int, db:Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_user_id(user_id=user_id)

@router.get("/id/{user_id}/page/{page}", status_code=201)
async def get_articles_by_title(title:str,page:int, db:Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_articles_by_title(title=title)
