from api.api_logging import logger
from typing import Annotated
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from api.functions import get_note_by_name, list_files_in_directory, notes_view
from api.markdown import html, text_index
from jinja2_fragments.fastapi import Jinja2Blocks


router = APIRouter(prefix="/note", tags=["note"])
templates = Jinja2Blocks(directory="templates")


def hx(request: Request) -> bool:
    return request.headers.get("HX-Request")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, name: str = None):
    logger.info(["home"])
    if name:
        text = get_note_by_name(name)
        return templates.TemplateResponse(
            "note.html", {
                "request": request,
                "note_name": name,
                "index": text_index(text),
                "note_content": html(text),
            },
            block_name="content" if hx(request) else None,
        )
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "notes_list": list_files_in_directory("../../notes/z/"),
            "notes_view": notes_view(),
        },
        block_name="content" if hx(request) else None,
    )


@router.post("/", response_class=HTMLResponse)
async def save_note(request: Request, name: str, note_content: str = None):
    logger.info([name, note_content])
    logger.info([*request.headers.items()])


@router.get("/edit/", response_class=HTMLResponse)
async def edit_note(request: Request, name: str):
    logger.info(["search", name])
    return templates.TemplateResponse("edit_note.html", {
        "request": request,
        "note_name": name,
        "note_content": get_note_by_name(name)
    },
        block_name="content" if hx(request) else None,
    )


@router.post("/search/", response_class=HTMLResponse)
async def search_note(request: Request, name: Annotated[str, Form()]):
    logger.info(["search", name])
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
