from fastapi import APIRouter, Depends, Query
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate, add_pagination, LimitOffsetPage, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from app.cruds.user import UserCrud
from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import current_time
from app.database import get_db
from app.schemas.user import UserDTO, UserUpdate, PageUser

router = APIRouter()

@router.post("/join", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).add_user(request_user=dto)))

@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).login_user(request_user=dto)))
@router.post("/logout", status_code=200)
async def logout_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).logout_user(request_user=dto)))

@router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify")
async def modify_user(dto: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.put("/reset-password")
async def reset_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).reset_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)
@router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).delete_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.get("/page/{page}/size/{size}",response_model=Page[PageUser])
async def get_users_per_page(page: int, size=int, db: Session = Depends(get_db)):
    params = Params(page=page,size=size)
    results = UserCrud(db).find_all_users_per_page(page)
    page_result = paginate(results,params)
    count = UserCrud(db).count_all_users()
    dc = {"page": page_result, "count": count}
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(dc))


'''@router.get("/email/{id}")
async def get_user(id: str, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_user_by_id(id, db)
    return {"data": "success"}'''

@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_users_by_job(search, page,db)
    return {"data": "success"}
