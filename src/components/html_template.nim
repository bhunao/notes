import karax / [karaxdsl, vdom]



proc htmlTemplate*(content: string = "coisa"): string =
    var res = buildHtml(html):
        head:
            meta(charset="utf-8")
            meta(name="viewport", content="width=device-width, initial-scale=1")
            title: text "Notes"
            script(src="https://unpkg.com/htmx.org@1.9.4", integrity="sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV", crossorigin="anonymous")
            link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9", crossorigin="anonymous")

        body:
            nav(class="navbar navbar-dark bg-dark"):
                tdiv(class="container-fluid"):
                    a(class="navbar-brand"):
                        text "Notes"

                    form(class="d-flex", role="search", hx-post="/search/", hx-target="#content", hx-swap="inner"):
                        input(class="form-control me-2", type="search", placeholder="Search", aria-label="Seasdarch", id="note_name", name="name", `required`="")
                        button(class="btn btn-light", type="submit"):
                            text "Search"

            tdiv(class="row border-end"):
                tdiv(class="col-2 p-3"):
                    tdiv(id="simple-list-example", class="d-flex flex-column gap-1 simple-list-example-scrollspy text-center"):
                        a(class="p-1 rounded", href="#simple-list-item-1"):
                            text "Item 1"

                tdiv(class="col-10 border-start"):
                    tdiv(id="content", data-bs-spy="scroll", data-bs-target="#simple-list-example", data-bs-offset="0", data-bs-smooth-scroll="true", class="scrollspy-example", tabindex="0"):
                        verbatim content

            script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js", integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm", crossorigin="anonymous")
    result = $res
