import db_connector/db_sqlite
import std/math


proc getRow*(name, path: string): seq[Row] =
  let db = open("mytest.db", "", "", "")
  result = db.getAllRows(
    sql"SELECT * FROM notes WHERE name = ? and path = ?", name, path
  )
  db.close()

proc insertRow*(name, path: string) =
  let db = open("mytest.db", "", "", "")
  db.exec( sql"INSERT INTO notes (name, path) VALUES (?, ?)", name, path
  )
  db.close()

