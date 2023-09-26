import karax / [karaxdsl, vdom]

proc testComponent*(cont: string): string =
    var res = buildHtml(html):
        head:
            script(src="https://unpkg.com/htmx.org@1.9.4", integrity="sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV", crossorigin="anonymous")
            link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9", crossorigin="anonymous")
        body:
            tdiv(class="d-flex", id="wrapper"):
                tdiv(class="border-end bg-white", id="sidebar-wrapper"):
                    tdiv(class="sidebar-heading border-bottom bg-light"):
                        text "Start Bootstrap"
                    tdiv(class="list-group list-group-flush"):
                        a(class="list-group-item list-group-item-action list-group-item-light p-3", href="#!"):
                            text "Dashboard"
                tdiv(id="page-content-wrapper"):
                    nav(class="navbar navbar-expand-lg navbar-light bg-light border-bottom"):
                        tdiv(class="container-fluid"):
                            button(class="btn btn-primary", id="sidebarToggle"):
                                text "Toggle Menu"
                            button(class="navbar-toggler", type="button", data-bs-toggle="collapse", data-bs-target="#navbarSupportedContent", aria-controls="navbarSupportedContent", aria-expanded="false", aria-label="Toggle navigation"):
                                span(class="navbar-toggler-icon")
                            tdiv(class="collapse navbar-collapse", id="navbarSupportedContent"):
                                ul(class="navbar-nav ms-auto mt-2 mt-lg-0"):
                                    li(class="nav-item active"): a(class="nav-link", href="#!"): text "Home"
                                    li(class="nav-item active"): a(class="nav-link", href="#!"): text "Home"
                                    li(class="nav-item active"): a(class="nav-link", href="#!"): text "Home"
                                    li(class="nav-item active"): a(class="nav-link", href="#!"): text "Home"
                    tdiv(class="container-fluid"):
                        tdiv(id="content"):
                            verbatim(cont)

                    a(`hx-get`="/note/", `hx-swap`="innerHTML", `hx-target`="#content"):
                        button(class="btn btn-dark"):
                            text "DARK BUTAOAS"
            


            script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js", integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm", crossorigin="anonymous")
    result = $res

