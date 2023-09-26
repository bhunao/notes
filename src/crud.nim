import db_connector/db_sqlite
import std/math


proc getRowById*(id: int): Row =
  let db = open("mytest.db", "", "", "")
  result = db.getRow(
    sql"SELECT * FROM notes WHERE id = ?", id
  )
  db.close()

proc getRow*(name, path: string): seq[Row] =
  let db = open("mytest.db", "", "", "")
  result = db.getAllRows(
    sql"SELECT * FROM notes WHERE name = ?", name
  )
  db.close()

proc insertRow*(name, path: string) =
  let db = open("mytest.db", "", "", "")
  db.exec( sql"INSERT INTO notes (name, path) VALUES (?, ?)", name, path
  )
  db.close()

