# Import HappyX
import
  happyx,
  path_params

# Serve at http://127.0.0.1:5000
serve("127.0.0.1", 5000):
  # on GET HTTP method at http://127.0.0.1:5000/
  get "/":
    # Return plain text
    buildHtml(html):
      head:
        script(src="https://unpkg.com/htmx.org@1.9.4", integrity="sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV", crossorigin="anonymous")
        link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9", crossorigin="anonymous")
      body:
        a(`hx-get`="/note/", `hx-swap`="innerHTML", `hx-target`="#content"):
          button(class="btn btn-dark"):
            "DARK BUTAOAS"
        tdiv(id="content")
        script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js", integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm", crossorigin="anonymous")

  # on any HTTP method at http://127.0.0.1:5000/public/path/to/file.ext
  get "/note/":
    buildHtml(`div`):
      tdiv(id="content"):
        for x in @["ASLDKFJN", "ADSKF", "LKKKJHASDASDQWD"]:
          "2345"
          br

  staticDir "public"

