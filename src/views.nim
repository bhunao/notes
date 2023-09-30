import std/os
import prologue
import ./components/[note, edit_note, search, html_template]
import db_connector/db_sqlite
import ./utils
import markdown


proc getIndex*(ctx: Context) {.async.} =
  # TODO: add stuff to index template
  resp htmlTemplate()

proc getNote*(ctx: Context) {.async.} =
  # TODO: return note content inside a htmlNote
  echo "============ getNote ============"
  echo ctx.getPathParams("id")
  var id = ctx.getPathParams("id")

  let db = open("mytest.db", "", "", "")
  var row = db.getRow( sql"SELECT * FROM notes WHERE id = ?", id)
  db.close()

  if row[0] == "":
    resp "invalid id", Http404
  else:
    var 
      note = openNote(row[2] / row[1].addFileExt ".md" )
      config = markdown.initGfmConfig()
      html = markdown(note, config)
    resp htmlTemplate html

proc postNote*(ctx: Context) {.async.} =
  # TODO: save the content to the file and update in database
  echo "============ postNote ============"
  echo ctx.getFormParams("name")
  echo ctx.getFormParams("path")
  echo ctx.getFormParams("content")
  echo "============ ======== ============"
  resp htmlTemplate()

proc postSearch*(ctx: Context) {.async.} =
  # TODO: get search results and return them
  echo ctx.request
  echo ctx.getFormParams("name")
  var name = ctx.getFormParams("name")
  resp htmlSearch()

proc getEdit*(ctx: Context) {.async.} =
  # TODO: get note content inside a htmlEditNote
  resp htmlTemplate()
