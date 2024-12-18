from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    uuid: str | None = None
    name: str
    email: str
    phone: str | None = None
    avatar: str | None = None
    geo: dict = Field(default_factory=dict)
    timezone: str | None = None
    language: str | None = None
    password: str
    status: int = Field(default=0)
    register_time: datetime | None = Field(default_factory=datetime.utcnow)