import db_connector/db_sqlite
import std/math

let db* = open("mytest.db", "", "", "")

db.exec(sql"DROP TABLE IF EXISTS notes")
const CREATEDB = """
create table if not exists `notes` (
  `id` integer not null primary key autoincrement,
  `name` VARCHAR(255) not null,
  `path` varchar(255) not null,
  `created_at` datetime null default CURRENT_TIMESTAMP, 
  `last_update` datetime null default CURRENT_TIMESTAMP,
  `parent` varchar(255) null,
  `type` varchar(255) null
);
"""
db.exec(sql"DROP TABLE IF EXISTS notes")
const COISA = """
CREATE TABLE my_table (
                 id    INTEGER PRIMARY KEY,
                 name  VARCHAR(50) NOT NULL,
                 i     INT(11),
                 f     DECIMAL(18, 10)
              )
"""

  

db.exec(sql CREATEDB)

db.close()
