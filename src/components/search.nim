import karax / [karaxdsl, vdom]
import db_connector/db_sqlite


proc htmlSearch*(content: seq[Row] = @[]): string =
  var res = buildHtml(tdiv):
    tdiv(class="container p-3", id="content"):

      tdiv(class="list-group"):
        for row in content:
            a(href="", hx-get="/note/"&row[0], hx-target="#content", hx-push-url="true", class="list-group-item list-group-item-action"):
              tdiv(class="d-flex w-100 justify-content-between"):
                h5(class="mb-1"): text row[1]
                small(class="text-body-secondary"): text row[4]

              p(class="mb-1"): text row[0]
              small(class="text-body-secondary"): text row[2]

      hr(class="p-5")

  result = $res
