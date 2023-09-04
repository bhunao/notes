import logging
from typing import Annotated
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from api.functions import get_note_by_name
from api.markdown import html, text_index
from jinja2_fragments.fastapi import Jinja2Blocks


router = APIRouter(prefix="/note", tags=["note"])
templates = Jinja2Blocks(directory="templates")


def hx(request: Request) -> bool:
    return request.headers.get("HX-Request")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logging.info("home")
    print("HOME")
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
        },
        block_name="content" if hx(request) else None,
    )


@router.get("/edit/", response_class=HTMLResponse)
async def edit_note(request: Request, name: str):
    print(*request.headers.items(), "\n")
    logging.info("EDIT NOTE")
    print("EDIT_note", name, hx(request))
    return templates.TemplateResponse("edit_note.html", {
        "request": request,
        "note_name": name,
        "note_content": get_note_by_name(name)
    },
        block_name="content" if hx(request) else None,
    )


@router.get("/{name}", response_class=HTMLResponse)
async def get_note(request: Request, name: str):
    return templates.TemplateResponse(
        "edit_note.html", {
            "request": request,
            "note_name": name,
            "note_content": get_note_by_name(name)
        },
        block_name="content" if hx(request) else None,
    )


@router.post("/search/", response_class=HTMLResponse)
async def search_note(request: Request, name: Annotated[str, Form()]):
    print("SEARCH", name, hx(request))
    # TODO -> search algorithm
    content = get_note_by_name(name)
    index = text_index(content)
    content = html(content)
    return templates.TemplateResponse(
        "note.html", {
            "request": request,
            "note_name": name,
            "index": index,
            "note_content": content,
        },
        block_name="content" if hx(request) else None,
    )
