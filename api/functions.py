import os
from fastapi import HTTPException
from logging import getLogger
from api.crud import create_note, query


log = getLogger(__name__)
directory_path = "../../notes/z/"
note_names = []


def list_files_in_directory(path):
    global note_names
    file_list = []
    new_notes_names = []
    for root, directories, files in os.walk(path):
        for file in files:
            file_list.append(file[:-3])
            new_notes_names.append(file)
            name = file[:-3]
            path = root[len(directory_path):]
            if not query({"name": name, "path": path}):
                create_note(name, path)
                log.info(f"created note {name} with path {path}")
                print(name, path)
    note_names = new_notes_names
    return file_list


def get_note_by_name(name: str) -> str:
    name += ".md"
    if name.lower() in note_names:
        for root, directories, files in os.walk(directory_path):
            for file in files:
                if file.lower() == name.lower():
                    log.info([f"file '{name}' found"])
                    with open(os.path.join(root, file), 'r') as file:
                        return file.read()
    log.error(["FILE NOT FOUND"])
    raise HTTPException(
        status_code=404,
        detail=f"no note with the name '{name}'"
    )


def notes_view():
    file_list = []
    for root, directories, files in os.walk(directory_path):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                text = f.read()
            max_len = 300
            values = file[:-3], text[:max_len or 50]
            file_list.append(values)
    return file_list


def get_note(path, name):
    full_path = os.path.join(directory_path, path, name) + ".md"
    with open(full_path) as file:
        return file.read()


all_files = list_files_in_directory(directory_path)
