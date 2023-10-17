from sqlmodel import column
from . import domain, models
from fastapi.responses import HTMLResponse
from jinja2_fragments.fastapi import Jinja2Blocks
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static/"), name="static")
templates = Jinja2Blocks(directory="backend/frontend")


@app.get("/", response_class=HTMLResponse)
async def get_all_notes(request: Request, page: int = 0, limit=10):
    notes_content = domain.get_all(page * limit, limit=limit)
    return templates.TemplateResponse(
        "components/index.html",
        {
            "request": request,
            "notes": notes_content,
        },
        block_name=None
    )


@app.get("/{note_name}", response_class=HTMLResponse)
async def get_note(request: Request, note_name: str):
    note = models.Note(name=note_name, path="")
    note_content = domain.get_html(note)
    return templates.TemplateResponse(
        "components/note.html",
        {
            "request": request,
            "note": note,
            "note_content": note_content
        },
        block_name=None
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
        block_name=None
    )


@app.get("/note/new/", response_class=HTMLResponse)
async def new_note(request: Request):
    return templates.TemplateResponse(
        "components/new.html",
        {
            "request": request,
        },
        block_name=None
    )


@app.get("/search/{note_name}", response_class=HTMLResponse)
async def search_notes(request: Request, note_name: str, offset: int = 0, limit:int = 10):
    notes_content = domain.get_all_where(column("name").contains(note_name))
    print(*[n for n in notes_content], sep="")
    return templates.TemplateResponse(
        "components/search.html",
        {
            "request": request,
            "notes": notes_content,
        },
        block_name=None
    )
