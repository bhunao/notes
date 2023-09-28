import prologue
import ./components/[note, edit_note, search, html_template]


proc getIndex*(ctx: Context) {.async.} =
  # TODO: add stuff to index template
  resp htmlTemplate()

proc getNote*(ctx: Context) {.async.} =
  # TODO: return note content inside a htmlNote
  echo "============ getNote ============"
  echo ctx.getPathParams("id")
  resp htmlTemplate()

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
  resp htmlSearch()

proc getEdit*(ctx: Context) {.async.} =
  # TODO: get note content inside a htmlEditNote
  resp htmlTemplate()
