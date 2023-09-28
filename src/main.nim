import happyx
import crud
import utils
import std/os
import std/strutils
import markdown
import components/html_template
import std/strformat
import components/note
import components/search
import components/edit_note


proc isHxRequest(req: Request): bool =
  if req.headers.hasKey("hx-request"):
    return req.headers["hx-request"] == "true"
  else:
    return false

serve("127.0.0.1", 5000):
  post "/edit/{id:int}":
    echo "======================================="
    echo "body: ", happyx.parseXWwwFormUrlencoded(req.body)
    echo "======================================="

    var 
      row = getRowById(id)
      path = row[2] / row[1].addFileExt "md"
      notes_dir = getEnv("NOTES_DIR")
      fullPath = notes_dir / path
      body = parseXWwwFormUrlencoded(req.body)
      content = body["content"]

    # saveNote(row, content)
    var
      html = openNote(path)
      note = markdown $htmlNote(row, content)

    if req.headers.hasKey("hx-request"):
      answerHtml(req, note, Http200)
    else:
      answerHtml(req, $htmlTemplate(note), Http200)

  get "/edit/{id:int}":
    echo fmt"got edit stuff"
    var 
      row = getRowById(id)
      fullPath = row[2] / row[1].addFileExt "md"
      html = openNote(fullPath)
      editNote = $htmlEditNote(row, html)

      
    if isHxRequest(req):
      answerHtml(req, editNote, Http200)
    else:
      answerHtml(req, $htmlTemplate(editNote), Http200)

  get "/":
    answerHtml(req, $htmlTemplate(), Http200)
  post "/search/":
    var 
      name = happyx.parseXWwwFormUrlencoded(req.body)["name"].addFileExt "md"
      result = getRow(name, "")
    
    if result.len == 1:
      var 
        row = result[0]
        fullPath = row[2] / row[1].addFileExt "md"
        config = markdown.initGfmConfig()
        html = markdown(openNote(fullPath), config)
      if isHxRequest(req):
        answerHtml(req, $htmlNote(row, html), Http200)
      else:
        answerHtml(req, $htmlTemplate(html), Http200)
    else:
      answerHtml(req, $htmlSearch(result), Http200)

  get "/note/{id:int}":
    echo fmt"notes {id}"
    var 
      row = getRowById(id)
      fullPath = row[2] / row[1].addFileExt "md"
      config = markdown.initGfmConfig()
      html = markdown(openNote(fullPath), config)
      note = $htmlNote(row, html)
      
    if req.headers.hasKey("hx-request"):
      answerHtml(req, $htmlNote(row, html), Http200)
    else:
      answerHtml(req, $htmlTemplate(note), Http200)
    

  # on any HTTP method at http://127.0.0.1:5000/public/path/to/file.ext
  staticDir "public"

