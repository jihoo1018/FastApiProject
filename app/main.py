import os
import sys
from fastapi_sqlalchemy import DBSessionMiddleware

from .database import init_db
from .env import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE, DB_URL

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter
from .routers.user import router as user_router
from .routers.article import router as article_router

router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
router.include_router(article_router, prefix="/article",tags=["article"])
app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

@app.get("/")
async def root():
    return {"message ": " Welcome Fastapi"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.on_event("startup")
async def on_startup():
    await init_db()