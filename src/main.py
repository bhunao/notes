from typing import List, Tuple
import database
import files
import models


def insert_note_metadata(files: List[Tuple[str, str]]):
    for name, path in files:
        new_note = models.Note(
            name=name,
            path=path,
        )
        database.create(new_note)


if __name__ == "__main__":
    lista = files.list_files_in_directory(files.directory_path)
    insert_note_metadata(lista)
