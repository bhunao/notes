import happyx
import crud
import utils
import std/os
import std/strutils
import markdown
import components/html_template
import components/note
import components/search
import components/edit_note

serve("127.0.0.1", 5000):
  get "/edit/{id:int}":
    echo "body: ", happyx.parseXWwwFormUrlencoded(req.body)
    var 
      row = getRowById(id)
      fullPath = row[2] / row[1].addFileExt "md"
      html = openNote(fullPath)
      editNote = $htmlEditNote(row, html)

      
    if req.headers.hasKey("hx-request"):
      answerHtml(req, editNote, Http200)
    else:
      answerHtml(req, $htmlTemplate(editNote), Http200)

  get "/":
    answerHtml(req, $htmlTemplate(), Http200)
  post "/search/":
    echo "body: ", happyx.parseXWwwFormUrlencoded(req.body)
    var 
      name = happyx.parseXWwwFormUrlencoded(req.body)["name"]
      isHxRequest = req.headers.hasKey("hx-request")
      result = getRow(name, "")
    
    if result.len == 1:
      var 
        row = result[0]
        fullPath = row[2] / row[1].addFileExt "md"
        config = markdown.initGfmConfig()
        html = markdown(openNote(fullPath), config)
      if isHxRequest:
        answerHtml(req, $htmlNote(row, html), Http200)
      else:
        answerHtml(req, $htmlTemplate(html), Http200)
    else:
      answerHtml(req, $htmlSearch(result), Http200)

  get "/note/{id:int}":
    var 
      row = getRowById(id)
      fullPath = row[2] / row[1].addFileExt "md"
      config = markdown.initGfmConfig()
      html = markdown(openNote(fullPath), config)
      note = $htmlNote(row, html)

      
    if req.headers.hasKey("hx-request"):
      answerHtml(req, note, Http200)
    else:
      answerHtml(req, $htmlTemplate(note), Http200)
    

  # on any HTTP method at http://127.0.0.1:5000/public/path/to/file.ext
  staticDir "public"

