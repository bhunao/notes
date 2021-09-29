from typing import List, Optional

from pydantic import BaseModel

class NoteBase(BaseModel):
    content: str
    priority: Optional[int] = None


class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    _deleted: Optional[bool] = False

    class Config:
        orm_mode = True
