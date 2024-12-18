import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# 创建 SQLModel 引擎
engine = create_engine(DATABASE_URL, echo=True)

# 异步数据库连接池
# SQLModel 目前并没有官方的异步支持，可以使用 SQLAlchemy 的 async 支持进行异步操作，但这里保持同步方式
def get_db():
    with Session(engine) as session:
        yield session