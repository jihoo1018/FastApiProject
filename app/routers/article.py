from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.repositories.article as pao
from app.schemas.article import Article

router = APIRouter()


@router.get("/{page}")
async def get_articles(page: int, db: Session = Depends(get_db)):
    ls = pao.find_article(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_post(id : str,db: Session = Depends(get_db)):
    pao.find_article(id=id,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{no}")
async def get_post_by_title(search: str, page: int, db: Session = Depends(get_db)):
    pao.find_article_by_title(search,page,db)
    return {"data":"sucess"}

@router.post("/")
async  def join(item: Article, db: Session = Depends(get_db)):
    article_dict = item.dict()
    print((f"SignUp Inform : {article_dict}"))
    pao.join(item=item,db=db)
    return {"data":"sucess"}

@router.post("/{id}")
async def login(id:str,item:Article, db: Session = Depends(get_db)):
    pao.login(id, item, db)
    return {"data": "success"}

@router.put("/{id}")
async def update(id:str,item: Article, db: Session = Depends(get_db)):
    pao.update(id=id,item=item,db=db)
    return {"data":"sucess"}

@router.delete("/{id}")
async def delete(id:str,user: Article, db: Session = Depends(get_db)):
    pao.delte(id=id,item=user,db=db)
    return {"data":"sucess"}