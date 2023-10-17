from datetime import datetime
from sqlmodel import Field, SQLModel
from typing import Optional


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: str
    parent: Optional[int] = None
    type: Optional[str] = None
    date_created: datetime = Field(default=datetime.now())
    last_edit: datetime = Field(default=datetime.now())
