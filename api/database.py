import sqlite3 as sql3

from contextlib import contextmanager
from logging import getLogger
from datetime import datetime


SQLITE_FILE = "notes.db"

log = getLogger(__name__)
con = sql3.connect(SQLITE_FILE)
cur = con.cursor()

with open("api/create.sql") as f:
    sql = f.read()
    for create_table in sql.split(";"):
        cur.execute(create_table)


@contextmanager
def db_cursor(*args, **kwds):
    con = sql3.connect("notes.db")
    cursor = con.cursor()

    try:
        yield cursor
    finally:
        con.commit()
        con.close()
