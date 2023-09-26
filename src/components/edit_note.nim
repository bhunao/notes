import karax / [karaxdsl, vdom]
import db_connector/db_sqlite


proc htmlEditNote*(row: Row, content: string): string =
  var res = buildHtml(tdiv):
    small(class="text-body-secondary"): text "last edit:" & row[4]

    tdiv(class="container p-3"):
      form(class="", role="search", hx-post="/search/", hx-target="#content", hx-swap="inner"):

        tdiv(class="mb-3"):
          label(`for`="note_name", class="form-label"): text "name"
          input(class="form-control me-2", type="search", placeholder=row[1], aria-label="Seasdarch", id="note_name", name="name", `required`="")


        tdiv(class="mb-3"):
          label(`for`="note_path", class="form-label"): text "path"
          input(class="form-control me-2", type="search", placeholder=row[2], aria-label="Seasdarch", id="note_path", name="path", `required`="")

        tdiv(class="mb-3"):
          label(`for`="note_parent", class="form-label"): text "parent"
          input(class="form-control me-2", type="search", placeholder=row[3], aria-label="Seasdarch", id="note_parent", name="parent", `required`="")

        tdiv(class="mb-3"):
          label(`for`="note_content", class="form-label"): text "Example textarea"
          textarea(class="form-control", id="note_content", rows="10", name="textarea"): text content

        tdiv(class="container"):
          button(class="btn btn-light", type="submit"):
            text "Search"

  result = $res
