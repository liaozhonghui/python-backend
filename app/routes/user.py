from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Union
from app.db import get_db
from app.services.user import get_user_info

router = APIRouter(prefix='/user')

class LoginRequest(BaseModel):
    username: str
    password: str
    tags: Union[str, List[str]]  # tags 可以是字符串或字符串列表

@router.get('/user-info')
async def get_user_info_route(db=Depends(get_db)):
    user_info = await get_user_info(db)
    return user_info

@router.post('/login')
async def login(request: LoginRequest, db=Depends(get_db)):
    tags = request.tags
    # 判断 tags 的类型
    if isinstance(tags, str):
        return {"message": "login!", "username": request.username, "password": request.password, "tags": f"Single tag: {tags}"}
    elif isinstance(tags, list):
        return {"message": "login!", "username": request.username, "password": request.password, "tags": f"Multiple tags: {tags}"}
    else:
        return {"message": "login failed!", "error": "Invalid tags type"}