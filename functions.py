import os


directory_path = "../../notes/z/"
note_names = []

def list_files_in_directory(path):
    global note_names
    file_list = []
    new_notes_names = []
    for root, directories, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
            new_notes_names.append(file)
    note_names = new_notes_names
    return file_list

def get_note_by_name(name: str):
    name += ".md"
    if name.lower() in note_names:
        for root, directories, files in os.walk(directory_path):
            for file in files:
                if file.lower() == name.lower():
                    with open(os.path.join(root, file), 'r') as file:
                        c = file.read().split("\n")
                        return "<br>".join(c)
    else:
        return "not found"



all_files = list_files_in_directory(directory_path)

