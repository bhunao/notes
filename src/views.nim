import std/os
import prologue
import ./components/[note, edit_note, search, html_template]
import db_connector/db_sqlite
import ./utils
import markdown
import std/strformat


proc isHxRequest(ctx: Context): bool = ctx.request.hasHeader("hx-request")
proc isEmpty(row: Row): bool = row[0] == ""

proc getIndex*(ctx: Context) {.async.} =
  echo "========== get:index endpoint"
  let db = open("mytest.db", "", "", "")
  var rows = db.getAllRows( sql"SELECT * FROM notes")
  db.close()

  var content = htmlSearch(rows)

  resp if isHxRequest ctx: content else: htmlTemplate content

proc getNote*(ctx: Context) {.async.} =
  var id = ctx.getPathParams("id")

  echo "========== get:note endpoint"
  echo fmt"path parem id=[{id}]"

  let db = open("mytest.db", "", "", "")
  var row = db.getRow( sql"SELECT * FROM notes WHERE id = ?", id)
  db.close()

  if row.isEmpty:
    resp fmt"note with id=[{id}] not found", Http404

  var 
    note = openNote(row[2] / row[1].addFileExt ".md" )
    config = markdown.initGfmConfig()
    content = markdown(note, config)
  resp if isHxRequest ctx: content else: htmlTemplate content

proc postNote*(ctx: Context) {.async.} =
  # TODO: save the content to the file and update in database
  var
    name = ctx.getFormParams("name")
    path = ctx.getFormParams("path")
    content = ctx.getFormParams("content")

  echo "========== post:note endpoint"
  echo fmt"form param name=[{name}]"
  echo fmt"form param path=[{path}]"
  echo fmt"form param content=[{content}]"

  resp htmlTemplate()

proc postSearch*(ctx: Context) {.async.} =
  echo "========== post:search endpoint"
  var name = ctx.getFormParams("name").addFileExt ".md"

  let db = open("mytest.db", "", "", "")
  var rows = db.getAllRows( sql"SELECT * FROM notes WHERE name = ?", name)
  db.close()

  echo fmt"found {rows.len} notes whith the name {name}"

  if rows.len == 1:
    var 
      note = openNote(rows[0][2] / rows[0][1].addFileExt ".md" )
      config = markdown.initGfmConfig()
      content = markdown(note, config)

    resp if isHxRequest ctx: content else: htmlTemplate content

  else:
    resp htmlSearch(rows)


proc getEdit*(ctx: Context) {.async.} =
  # TODO: get note content inside a htmlEditNote
  echo "========== get:edit endpoint"
  resp htmlTemplate()
