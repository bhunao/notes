import happyx
import crud
import utils
import std/os
import std/strutils
import markdown
import components/html_template
import components/note

serve("127.0.0.1", 5000):
  get "/":
    answerHtml(req, $htmlTemplate(), Http200)
  get "/note/{name}":
    var result = getRow(name, "")
    echo result
    if result.len == 0:
      return "Hello, world!"          
    elif result.len == 1:
      var 
        row = result[0]
        fullPath = row[2] / row[1].addFileExt "md"
        config = markdown.initGfmConfig()
        html = $testComponent markdown(openNote(fullPath), config)
      answerHtml(req, html, Http200)

    else:
      return "more than 1 stuff"
    

  # on any HTTP method at http://127.0.0.1:5000/public/path/to/file.ext
  staticDir "public"

