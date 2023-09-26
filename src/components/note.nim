import karax / [karaxdsl, vdom]
import db_connector/db_sqlite


proc htmlNote*(row: Row, content: string): string =
  var res = buildHtml(tdiv):
    tdiv(class="container p-3"):
      verbatim(content)

      button(hx-get="/edit/"&row[0], hx-trigger="click", hx-target="#content", hx-swap="outerHTML", hx-push-url="true"):
        text "EDIT"

  result = $res
