from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functions import get_note_by_name, list_files_in_directory

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "notes_list": list_files_in_directory("../../notes/z/"),
        })

@app.get("/note/", response_class=HTMLResponse)
async def get_note(request: Request, name: str):
    note_name = name
    note_content = get_note_by_name(name)
    return templates.TemplateResponse(
        "note.html", {
            "request": request,
            "note_name": note_name,
            "note_content": note_content
        })
