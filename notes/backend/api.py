from . import domain, files, models
from fastapi import FastAPI, Request, Response
from fastapi import Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2_fragments.fastapi import Jinja2Blocks
from typing import Annotated
from markdown import markdown as toHtml


str_form = Annotated[str, Form()]

app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static/"), name="static")
templates = Jinja2Blocks(directory="backend/frontend")


def hx(request: Request) -> bool:
    return request.headers.get("hx-request") == "true"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, page: int = 0, limit: int = 10):
    notes = domain.get_notes_page(page, limit)
    for note in notes:
        note.content = toHtml(note.content)
    return templates.TemplateResponse(
        "components/index.html",
        {
            "request": request,
            "notes": notes
        },
        block_name="content" if hx(request) else None
    )


@app.get("/{id}", response_class=HTMLResponse)
async def get(request: Request, id: int):
    note = domain.get_note_with_id(id)
    note.content = toHtml(note.content)
    return templates.TemplateResponse(
        "components/note.html",
        {
            "request": request,
            "note": note,
        },
        block_name="content" if hx(request) else None
    )


@app.post("/{id}")
async def update(
        response: Response,
        id: int,
        name: Annotated[str, Form()],
        content: Annotated[str, Form()],
        path: Annotated[str, Form()] = "",
):
    domain.update_note_with_id(id, name, path, content)
    response.headers['hx-redirect'] = f"/{id}"
    response.headers['hx-push_url'] = "true"


@app.delete("/{id}", response_class=HTMLResponse)
async def delete(response: Response, id: int):
    response.headers['hx-redirect'] = "/"
    response.headers['hx-push_url'] = "true"
    domain.delete_note_with_id(id)


@app.get("/{id}/edit", response_class=HTMLResponse)
async def edit(request: Request, id: int):
    note = domain.get_note_with_id(id)
    return templates.TemplateResponse(
        "components/edit.html",
        {
            "request": request,
            "note": note,
        },
        block_name="content" if hx(request) else None
    )


@app.get("/new/", response_class=HTMLResponse)
async def create(request: Request):
    note = models.ResponseNote(name="sem_titulo", path="")
    return templates.TemplateResponse(
        "components/new.html",
        {
            "request": request,
            "note": note,
        },
        block_name="content" if hx(request) else None
    )


@app.post("/new/", response_class=HTMLResponse)
async def insert_new(
        request: Request,
        name: Annotated[str, Form()],
        content: Annotated[str, Form()],
        path: Annotated[str, Form()] = "",
):
    default_note = models.ResponseNote(
        name=name, path=path, content=content)
    note = domain.create_note(name, path, content)
    return templates.TemplateResponse(
        "components/new.html",
        {
            "request": request,
            "error": not note,
            "note": note if note else default_note,
        },
        block_name="content" if hx(request) else None
    )


@app.post("/search/", response_class=HTMLResponse)
async def search(request: Request, search_term: Annotated[str, Form()] = ""):
    notes = domain.search_note_like(search_term)
    for note in notes:
        note.content = toHtml(note.content)
    return templates.TemplateResponse(
        "components/index.html",
        {
            "request": request,
            "notes": notes
        },
        block_name="content" if hx(request) else None
    )


# =============================================================
@app.post("/insert/metadata/", response_class=JSONResponse)
async def post_insert_metadata():
    lista = files.list_files_in_directory(files.directory_path)
    domain.generate_note_metadata(lista)
    return {"true": True}
# =============================================================
