from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note)


@app.get("/notes/", response_model=list[schemas.Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes


@app.post("/notes/{name}", response_model=schemas.Note)
def get_by_name(name: str, db: Session = Depends(get_db)):
    note = crud.get_note_by_name(db, name)
    if note:
        return note
    raise HTTPException(status_code=400, detail="Email already registered")
