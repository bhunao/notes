import os
from api.api_logging import logger
from fastapi import HTTPException


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
    note_names = new_notes_names
    return file_list


def get_note_by_name(name: str) -> str:
    name += ".md"
    if name.lower() in note_names:
        for root, directories, files in os.walk(directory_path):
            for file in files:
                if file.lower() == name.lower():
                    logger.info([f"file '{name}' found"])
                    with open(os.path.join(root, file), 'r') as file:
                        return file.read()
    logger.error(["FILE NOT FOUND"])
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


all_files = list_files_in_directory(directory_path)
