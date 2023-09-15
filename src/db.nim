import db_connector/db_sqlite

let db = open("database/notes.db", "", "", "")

db.exec(sql readFile("database/create_tables.sql"))

db.crea

db.close()
