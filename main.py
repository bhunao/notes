from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functions import get_note_by_name

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request
        })

@app.get("/note/", response_class=HTMLResponse)
async def get_note(request: Request, name: str):
    print(name)
    note_name = name
    note_content = get_note_by_name(name)
    print(note_content)
    return templates.TemplateResponse(
        "note.html", {
            "request": request,
            "note_name": note_name,
            "note_content": note_content
        })
