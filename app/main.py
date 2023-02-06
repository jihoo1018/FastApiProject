import logging
import os
import sys

from fastapi_pagination import add_pagination
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from .admin.utils import current_time
from .database import init_db
from .env import DB_URL
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from .routers.user import router as user_router
from .test.user import router as test_router
from .admin.pagination import router as pagination_router
from .routers.article import router as article_router
from fastapi.security import APIKeyHeader
API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")
print(f" ################ app.main Started At {current_time()} ################# ")


router = APIRouter()
router.include_router(user_router, prefix="/user",tags=["user"])
router.include_router(article_router, prefix="/article",tags=["article"])
router.include_router(test_router, prefix="/test",tags=["test"])
router.include_router(pagination_router, prefix="/pagination",tags=["pagination"])
app = FastAPI()
add_pagination(app)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.get("/protected-router")
async def protected_route(token:str = Depends(api_key_header)):
    if token !=API_TOKEN:
        raise HTTPException(status_code=403)
    return {"403":"잘못된 경로입니다"}

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return HTMLResponse(content=f"""
    <body>
    <div >
        <h1 style="width: 400px; margin: 50 auto">
        {current_time()}<br/>
        현재 서버 구동중 입니다</h1>
    </div>
    </body>
    """)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
