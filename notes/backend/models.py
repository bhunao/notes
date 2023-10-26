from datetime import datetime
from sqlmodel import Field, SQLModel
from typing import Optional


class ResponseNote(SQLModel, table=False):
    id: Optional[int] = None
    name: str
    path: str
    parent: Optional[int] = None
    type: Optional[str] = None
    date_created: datetime = Field(default=datetime.now())
    last_edit: datetime = Field(default=datetime.now())
    content: str = Field(default="", exclude=True)


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: str
    parent: Optional[int] = None
    type: Optional[str] = None
    date_created: datetime = Field(default=datetime.now())
    last_edit: datetime = Field(default=datetime.now())
    # _content: str = Field(default="", exclude=True)

    def content(self, content: str) -> ResponseNote:
        return ResponseNote(
                id=self.id,
                name=self.name,
                path=self.path,
                parent=self.parent,
                type=self.type,
                date_created=self.date_created,
                last_edit=self.last_edit,
                content=content
                )
