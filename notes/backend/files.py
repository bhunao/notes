import database

from typing import List, Tuple
from pathlib import Path

from datetime import datetime
from os import walk, environ
from models import Note


directory_path = environ.get("NOTES_PATH")
print("directory path: ", directory_path)
note_names = []

assert directory_path is not None, "YOU NEED TO CREATE THE ENVIROMENT VARIABLE 'NOTES_PATH'"
assert Path(directory_path).is_dir(), "´NOTES_PATH´ ENVIROMENT VARIABLE IS NOT A DIR"


def validate_file(path: str):
    full_path = Path(path)
    if not full_path.is_file: raise FileNotFoundError()
    return full_path


def get_content(name: str, path: str) -> str:
    full_path = validate_file(f"{directory_path}{path}/{name}.md")
    with open(full_path) as file:
        return file.read()


def delete(name: str, path: str):
    full_path = validate_file(f"{directory_path}{path}/{name}.md")
    full_path.unlink()


def update_content(name: str, path: str, new_content: str) -> bool:
    full_path = validate_file(f"{directory_path}{path}/{name}.md")
    with open(full_path, "w") as file:
        file.write(new_content)
        return True


def create_if_not_exists(name: str, path: str):
    note = Note(name=name, path=path)
    note = database.select(note)

    if note is not None:
        return

    now = datetime.now()
    note = Note(
        name=name, path=path,
        date_created=now, last_edit=now,
        type="note"
    )
    database.create(note)


def list_files_in_directory(path) -> List[Tuple[str, str]]:
    file_list = []
    for root, _, files in walk(path):
        for file in files:
            name = file[:-3]
            path = root[len(directory_path):]
            file_list.append((name, path))
    return file_list


if __name__ == "__main__":
    me = get_content("me", "")

    assert me is not None

    new_content = "#coiso um dois tres\n- um dois  -um treis  --- alguma outra coisa"
    update_content("coiso", "", new_content)
    new_entry = get_content("coiso", "")

    assert new_entry == new_content

    delete("coiso", "")
    assert Path(f"{directory_path}{''}/{'coiso'}.md").exists() is False
