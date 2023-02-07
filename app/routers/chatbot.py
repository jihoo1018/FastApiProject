from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()

@router.get("/main", status_code=201)
async def get_chatbot(**request: str):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=request))