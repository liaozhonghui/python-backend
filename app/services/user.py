from app.entities.user import User
from sqlmodel import Session, select
from app.db import get_db

# 使用 async/await 获取数据库连接池中的连接
async def get_user_info(*, session: Session):
    # 使用 SQLModel 的查询方式进行数据库查询
    statement = select(User).limit(1)  # 获取第一个用户
    result = session.exec(statement)  # 执行查询
    user = result.first()  # 获取第一个结果
    return {"username": user.name, "email": user.email}