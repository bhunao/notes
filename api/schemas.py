from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    path: str | None = None
    parent: int | None = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
