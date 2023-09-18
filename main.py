from datetime import datetime
from os import walk
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: str
    date_created: datetime
    last_edit: datetime
    parent: Optional[int] = None
    type: Optional[str] = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


SQLModel.metadata.create_all(engine)

directory_path = "../../notes/z/"
note_names = []


def add_if_not_exists(name: str, path: str):
    with Session(engine) as session:
        statement = select(Note).where(
            Note.name == name,
            Note.path == path,
        )
        result = session.exec(statement).fetchall()
        if not result:
            now = datetime.now()
            session.add(
                Note(
                    name=name, path=path,
                    date_created=now, last_edit=now,
                ))
            session.commit()


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
