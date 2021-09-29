from typing import List, Optional

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
options = {1:"add",
           2:"read_all",
           3:"delete",
           4:"exit"}

def print_options(options: Optional[dict] = options):
    print(*options.items(), sep="\n")

def output_note(note: schemas.Note):
    lenght = len(note.content)
    print("_"*lenght)
    print(note.content)
    print(note.id, note.priority)
    print("="*lenght)

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

def main_loop():
    while True:
        print_options()
        entry = int(input("entry the number:"))
        print(options[entry])
        if entry == 4:
            print("bbye")
            exit()
        elif entry == 1:
            add()
        elif entry == 2:
            read_all()
        elif entry == 3:
            delete()
