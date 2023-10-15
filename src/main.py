from typing import List, Tuple
import database
import files
import models


def ppr(*args, **vargs):
    print("+"*50)
    print(*map(type, args))
    print(*args, **vargs)
    print("-"*50)


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

    database.select_all()
    one = models.Note(
        name="me",
        path="",
        parent=None,
    )
    one_result = database.select_note(one)[0]

    assert one_result is not None
    assert one_result.id is not None
    assert one_result.name == one.name
    assert one_result.path == one.path

    update_one = models.Note(
        name="me_dois_treissçdc",
        path="coisa/treco/",
        parent=None,
        type="bagui",
    )
    updated_id = one_result.id
    database.update_by_id(updated_id, update_one)
    after_update = database.select_by_id(updated_id)

    assert after_update is not None
    assert after_update.name == update_one.name
    assert after_update.type == update_one.type
