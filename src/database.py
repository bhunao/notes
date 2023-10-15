from datetime import datetime
from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.future import Engine
from typing import List
from models import Note

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)


def create(note: Note, _engine: Engine = engine):
    with Session(_engine) as session:
        session.add(note)
        session.commit()


def select_all(_engine: Engine = engine) -> List[Note]:
    with Session(_engine) as session:
        statement = select(Note)
        return [note for note in session.exec(statement)]


def select_note(note: Note, _engine: Engine = engine) -> List[Note]:
    with Session(_engine) as session:
        statement = select(Note).where(
            Note.name == note.name,
            Note.path == note.path,
            Note.parent == note.parent,
            Note.type == note.type,
        )
        result = session.exec(statement)
        return [note for note in result]


def select_by_id(id: int, _engine: Engine = engine) -> Note | None:
    with Session(_engine) as session:
        statement = select(Note).where(
            Note.id == id,
        )
        result = session.exec(statement).one_or_none()
        return result


def update_by_id(id: int, old_note: Note, _engine: Engine = engine) -> bool:
    with Session(_engine) as session:
        statement = select(Note).where(Note.id == id)
        note = session.exec(statement).one_or_none()
        if note is None:
            return False

        updatable_fields = ["name", "path", "parent", "type"]
        for field in updatable_fields:
            old_value = getattr(old_note, field)
            new_value = getattr(note, field)
            if new_value != old_value:
                setattr(note, field, old_value)
        note.last_edit = datetime.now()

        session.add(note)
        session.commit()
        session.refresh(note)
        return True
