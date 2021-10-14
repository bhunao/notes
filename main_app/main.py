from typing import List, Optional

from sqlalchemy.orm import Session

from . import crud, models, schemas, menu
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

options = ("add", "read_all", "delete", "exit")
def print_options(options: Optional[dict] = options):
    print(*options)

def main_loop():
    while True:
        print_options()
        entry = input("entry the number:")
        try:
            entry = int(entry)
        except:
            pass

        if entry == 4:
            menu.exit()
        elif entry == 1:
            menu.add()
        elif entry == 2:
            menu.read_all()
        elif entry == 3:
            menu.delete()
        elif entry in options:
            print(type(menu))
            func = getattr(menu, entry)
            func()
        else:
            print("no input option for", entry)
