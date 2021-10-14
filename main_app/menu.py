from . import crud, models, schemas
from .database import SessionLocal

from os import get_terminal_size


db = SessionLocal()

def output_note(note: schemas.Note):
    columns, lines = get_terminal_size()
    lenght = len(note.content)
    print("="*columns)
    print(note.content)
    print(note.id, note.priority)

def add():
    content = input("content: ")
    add = "init"
    while add != "":
        add = input()
        content += "\n" + add
    priority = int(input("priority: "))

    note = {"content":content, "priority":priority}

    note = crud.create_note(db=db, note=note)
    output_note(note)

def read_all():
    notes = crud.get_notes(db=db)
    
    for note in notes:
        output_note(note)

def delete():
    note_id = int(input("type the note id: "))
    note = crud.get_note(db=db, note_id=note_id)
    if note is None:
        print(f"no note with the id [{note_id}]")
        return

    output_note(note)
    areusure = input(
        f"are you sure you wanna delete the following note?(s/n)\n[{note.content} {note.priority}]\n")
    if areusure.lower() == "s":
        delete = crud.delete_note(db=db, note=note)
        print(delete)

def _exit():
    print("bbye")
    exit()
