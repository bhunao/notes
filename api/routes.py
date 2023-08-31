from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from functions import get_note_by_name, list_files_in_directory
from api.database import get_notes_desc, create_note_desc, all_notes_desc


router = APIRouter(prefix="/note", tags=["note"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_note(request: Request, name: str = None, edit: bool = False):
    if not name:
        n = all_notes_desc()
        return templates.TemplateResponse(
            "index.html", {
                "request": request,
                "notes_list": list_files_in_directory("../../notes/z/"),
            })
    if edit:
        return templates.TemplateResponse(
            "edit_note.html", {
                "request": request,
                "note_name": name,
                "note_content": get_note_by_name(name)
            })
    create_note_desc(name)
    return templates.TemplateResponse(
        "note.html", {
            "request": request,
            "note_name": name,
            "note_content": get_note_by_name(name)
        })


@router.post("/")
async def save_note(name: str, content: str):
    print(name)
    print(content)
    return name, content
