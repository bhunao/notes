from typing import List, Tuple
import database
import files
import models


def generate_note_metadata(files: List[Tuple[str, str]]):
    for name, path in files:
        new_note = models.Note(
            name=name,
            path=path,
        )
        database.create(new_note)


# domain stuff
def new(note: models.Note):
    files.create_if_not_exists(note.name, note.path)
    database.create(note)


def get(note: models.Note) -> List[models.Note]:
    files.get_content(note.name, note.path)
    result = database.select_note(note)
    return result


def get_all(note: models.Note) -> List[models.Note]:
    result = database.select_all()
    return result


def update(id: int, new_note: models.Note, content: str):
    note = database.select_by_id(id)
    if note is None:
        raise IndexError(f"no note with id {id}")
    files.update_content(note.name, note.path, content)
    database.update_by_id(id, new_note)


def delete(id: int):
    note = database.select_by_id(id)
    if note is None:
        raise IndexError(f"no note with id {id}")
    files.delete(note.name, note.path)
    database.delete_by_id(id)


if __name__ == "__main__":
    lista = files.list_files_in_directory(files.directory_path)
    generate_note_metadata(lista)
