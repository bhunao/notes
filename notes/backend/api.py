from . import domain, models, files
from fastapi import FastAPI, Request
from fastapi import Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2_fragments.fastapi import Jinja2Blocks
from sqlmodel import column
from typing import Annotated


app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static/"), name="static")
templates = Jinja2Blocks(directory="backend/frontend")


def hx(request: Request) -> bool:
    return request.headers.get("hx-request") == "true"


@app.get("/", response_class=HTMLResponse)
async def get_all_notes(request: Request, page: int = 0, limit: int = 10):
    notes_content = domain.get_all(page * limit, limit=limit)
    pages = [max(page-1, 0), page, page+1]
    return templates.TemplateResponse(
        "components/index.html",
        {
            "request": request,
            "notes": notes_content,
            "pages": pages
        },
        block_name="content" if hx(request) else None
    )


@app.get("/{note_name}", response_class=HTMLResponse)
async def get_note(request: Request, note_name: str):
    note = models.Note(name=note_name, path="")
    note_content = domain.get_html(note)
    print(f"note_id = {note.id=}")
    return templates.TemplateResponse(
        "components/note.html",
        {
            "request": request,
            "note": note,
            "note_content": note_content
        },
        block_name="content" if hx(request) else None
    )


@app.post("/{note_name}", response_class=HTMLResponse)
async def post_note(
        request: Request,
        name: Annotated[str, Form()],
        content: Annotated[str, Form()],
        path: Annotated[str, Form()] = "",
):
    note = models.Note(name=name, path=path)
    note = domain.get_all_where(
        models.Note.name == name
    )[0]
    assert note.id
    domain.update(note.id, note, content)
    note_content = domain.get_html(note)
    return templates.TemplateResponse(
        "components/note.html",
        {
            "request": request,
            "note": note,
            "note_content": note_content
        },
        block_name="content" if hx(request) else None
    )


@app.get("/{note_name}/edit", response_class=HTMLResponse)
async def edit_note(request: Request, note_name: str):
    note = models.Note(name=note_name, path="")
    note_content = domain.get(note)
    return templates.TemplateResponse(
        "components/edit.html",
        {
            "request": request,
            "note": note,
            "note_content": note_content
        },
        block_name="content" if hx(request) else None
    )


@app.get("/note/new/", response_class=HTMLResponse)
async def new_note(request: Request):
    return templates.TemplateResponse(
        "components/new.html",
        {
            "request": request,
        },
        block_name="content" if hx(request) else None
    )


@app.post("/search/", response_class=HTMLResponse)
async def search_notes(request: Request, name: Annotated[str, Form()] = ""):
    notes_data = domain.get_all_where(column("name").contains(name))
    return templates.TemplateResponse(
        "components/search.html",
        {
            "request": request,
            "notes": notes_data,
        },
        block_name="content" if hx(request) else None
    )


@app.post("/insert/metadata/", response_class=JSONResponse)
async def post_insert_metadata():
    lista = files.list_files_in_directory(files.directory_path)
    domain.generate_note_metadata(lista)
    return { "true": True}

