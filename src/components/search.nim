import karax / [karaxdsl, vdom]
import db_connector/db_sqlite


proc htmlSearch*(content: seq[Row] = @[]): string =
  var res = buildHtml(tdiv):
    tdiv(class="container p-3"):

      tdiv(class="list-group"):
        for row in content:
            a(href="#", class="list-group-item list-group-item-action"):
              tdiv(class="d-flex w-100 justify-content-between"):
                h5(class="mb-1"): text row[1]
                small(class="text-body-secondary"): text row[4]

              p(class="mb-1"): text row[0]
              small(class="text-body-secondary"): text row[2]

      hr(class="p-5")

      form(class="", role="search", hx-post="/search/", hx-target="#content", hx-swap="inner"):

        tdiv(class="mb-3"):
          label(`for`="note_name", class="form-label"): text "name"
          input(class="form-control me-2", type="search", placeholder="Search", aria-label="Seasdarch", id="note_name", name="name", `required`="")

        tdiv(class="mb-3"):
          label(`for`="note_path", class="form-label"): text "path"
          input(class="form-control me-2", type="search", placeholder="Search", aria-label="Seasdarch", id="note_path", name="path", `required`="")

        tdiv(class="mb-3"):
          label(`for`="note_parent", class="form-label"): text "parent"
          input(class="form-control me-2", type="search", placeholder="Search", aria-label="Seasdarch", id="note_parent", name="parent", `required`="")

        tdiv(class="mb-3"):
          label(`for`="note_content", class="form-label"): text "Example textarea"
          textarea(class="form-control", id="note_content", rows="10", name="textarea")

        tdiv(class="container"):
          button(class="btn btn-light", type="submit"):
            text "Search"

  result = $res
