from typing import Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def get_search_notes(db: Session, text: str):
    return db.query(models.Note).filter(text in models.Note.content).all()

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db:Session, note: schemas.Note):
    db.delete(note)
    db.commit()
    return f"note id[{note.id}] deleted"
