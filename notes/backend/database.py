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
        session.refresh(note)


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


def update_by_id(id: int, new_note: Note, _engine: Engine = engine) -> bool:
    with Session(_engine) as session:
        statement = select(Note).where(Note.id == id)
        note = session.exec(statement).one_or_none()
        if note is None:
            return False

        updatable_fields = ["name", "path", "parent", "type"]
        for field in updatable_fields:
            new_value = getattr(new_note, field)
            old_value = getattr(note, field)
            if old_value != new_value:
                setattr(note, field, new_value)
        note.last_edit = datetime.now()

        session.add(note)
        session.commit()
        session.refresh(note)
        return True


def delete_by_id(id: int, _engine: Engine = engine):
    with Session(_engine) as session:
        statement = select(Note).where(Note.id == id)
        to_delete = session.exec(statement).one_or_none()

        if to_delete is None: raise KeyError(f"no note with id: {id}")

        session.delete(to_delete)
        session.commit()


if __name__ == "__main__":
    select_all()
    test_note = Note(name="teste_nome", path="/test_dir")
    create(test_note)

    selected_one = select_note(test_note)[0]
    assert selected_one is not None
    assert selected_one.id is not None

    test_note.name = "teste_nome_02"
    test_note.path = "/teste_dir_02"

    update_by_id(selected_one.id, test_note)
    selected_one = select_note(test_note)[0]
    assert selected_one is not None
    assert selected_one.id is not None
    assert selected_one.name == "teste_nome_02"
    assert selected_one.path == "/teste_dir_02"

    delete_by_id(selected_one.id)
    assert select_note(selected_one) == []
