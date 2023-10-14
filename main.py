from datetime import datetime
from os import name, walk
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import List, Optional


def ppr(*args, **vargs):
    print("+"*50)
    print(*map(type, args))
    print(*args, **vargs)
    print("-"*50)


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: str
    parent: Optional[int] = None
    type: Optional[str] = None
    date_created: datetime
    last_edit: datetime


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


SQLModel.metadata.create_all(engine)

directory_path = "../../notes/z/"
note_names = []

def create(note: Note):
    with Session(engine) as session:
        session.add(note)
        session.commit()

def select_all() -> List[Note]:
    with Session(engine) as session:
        statement = select(Note)
        return [note for note in session.exec(statement)]

def select_one(note: Note) -> Note | None:
    with Session(engine) as session:
        statement = select(Note).where(
                    Note.name == note.name,
                    Note.path == note.path,
                    Note.parent == note.parent,
                    Note.type == note.type,
                )
        result = session.exec(statement).one_or_none()
        ppr(result.id)
        return result

def select_by_id(id: int) -> Note | None:
    with Session(engine) as session:
        statement = select(Note).where(
                    Note.id == id,
                )
        result = session.exec(statement).one_or_none()
        return result

def update_by_id(id: int, old_note: Note) -> bool:
    with Session(engine) as session:
        statement = select(Note).where(Note.id == id)
        note = session.exec(statement).one_or_none()
        if note is None: return False

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


def add_if_not_exists(name: str, path: str):
    with Session(engine) as session:
        statement = select(Note).where(
            Note.name == name,
            Note.path == path,
        )
        result = session.exec(statement).fetchall()
        if not result:
            now = datetime.now()
            note = Note(
                    name=name, path=path,
                    date_created=now, last_edit=now,
                    type="note"
                )
            create(note)


def list_files_in_directory(path):
    global note_names
    file_list = []
    new_notes_names = []
    for root, directories, files in walk(path):
        for file in files:
            file_list.append(file[:-3])
            new_notes_names.append(file)
            name = file[:-3]
            path = root[len(directory_path):]
            add_if_not_exists(name, path)

    note_names = new_notes_names
    return file_list


lista = list_files_in_directory(directory_path)
print("""
      ====================
      mano
      ====================


      """)
select_all()
one = Note(
        name="me",
        path="",
        parent=None,
        type="note",
        date_created=datetime.now(),
        last_edit=datetime.now(),
        )
one_result = select_one(one)
ppr(one_result)

assert one_result is not None
assert one_result.id is not None
assert one_result.name == one.name
assert one_result.path == one.path

update_one = Note(
        name="me_dois_treissçdc",
        path="coisa/treco/",
        parent=None,
        type="bagui",
        date_created=datetime.now(),
        last_edit=datetime.now(),
        )
updated_id = one_result.id
update_by_id(updated_id, update_one)
after_update = select_by_id(updated_id)
assert  after_update is not None
assert  after_update.name == update_one.name
assert  after_update.type == update_one.type
