from datetime import datetime
from . import models, files, database

from typing import List, Tuple

from sqlmodel import column


def generate_note_metadata(files: List[Tuple[str, str]]):
    """read all notes from the markdown files"""
    for name, path in files:
        new_note = models.Note(
            name=name,
            path=path,
        )
        database.create(new_note)


def add_content(note: models.Note) -> models.ResponseNote:
    content = files.get_content(note.name, note.path)
    return models.ResponseNote(
        id=note.id,
        name=note.name,
        path=note.path,
        parent=note.parent,
        type=note.type,
        date_created=note.date_created,
        last_edit=note.last_edit,
        content=content
    )

# ==================================================

def get_notes_page(page: int, per_page: int) -> List[models.ResponseNote]:
    """index"""
    notes = database.select_all(page*per_page, per_page)
    result = [add_content(note) for note in notes]
    return result


def get_note_with_id(id: int):
    """get"""
    note = database.select_by_id(id)

    if note is None:
        raise ValueError(f"invalid id, the number '{id}' is not valid")

    result = add_content(note)
    return result


def update_note_with_id(id: int, name: str, path: str, content: str):
    """update"""
    note = database.select_by_id(id)
    if note is None:
        raise ValueError(f"invalid id, the number '{id}' is not valid")
    files.update_content(name, path, content)

    note.name = name
    note.path = path
    note.last_edit = datetime.now()
    database.update(note)


def create_note(name: str, path: str, content: str) -> models.ResponseNote | None:
    """create"""
    select_all = database.select_all_where(
        models.Note.name == name,
        models.Note.content == content
    )
    # TODO: add loggin in this
    print(*select_all, sep=" -=-=-=-=-=-=-=-=-\n")
    if len(select_all) > 0:
        return None

    note = models.Note(name=name, path=path)
    new_note = database.create(note)
    files.update_content(name, path, content)
    result = add_content(new_note)
    return result


def search_note_like(search_term: str) -> List[models.ResponseNote]:
    """search"""
    notes = database.select_all_where(column("name").contains(search_term))
    result = [add_content(note) for note in notes]
    return result


def delete_note_with_id(id: int):
    """delete"""
    note = database.select_by_id(id)
    if note is None:
        raise IndexError(f"no note with id {id}")
    files.delete(note.name, note.path)
    database.delete_by_id(id)
