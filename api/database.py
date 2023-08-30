import sqlite3 as sql3
from typing import List
from datetime import datetime


from api.api_logging import logger


con = sql3.connect("notes.db")
cur = con.cursor()
# cur.execute("CREATE TABLE note(name, created_at, last_update)")



async def all_notes_desc():
    res = cur.execute("select * from note")
    return res.fetchall()

async def get_notes_desc(name: str):
    with con:
        res = con.execute("select * from note where name = ?", name)
        return res.fetchone()

async def create_note_desc(name: str):
    data = (name, datetime.now(), datetime.now())
    with con:
        res = con.execute("INSERT INTO note VALUES (?)", data)
        return res.fetchone()


async def get_all_documents() -> List[dict]:
    return


async def get_document(id: str) -> dict:
    return


async def get_document_by_name(name: str) -> dict:
    return


async def add_document(document_data: dict) -> dict:
    return


async def put_document(id: str, data: dict) -> dict:
    return


async def del_document(id: str) -> dict:
    return
