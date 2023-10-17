from fastapi.responses import HTMLResponse
from jinja2_fragments.fastapi import Jinja2Blocks
import domain
import models
from fastapi import FastAPI, Request

app = FastAPI()
templates = Jinja2Blocks(directory="../frontend/")


@app.get("/{note_name}")
async def read_items(request: Request, note_name: str):
    note = models.Note(name=note_name, path="")
    result = domain.get(note)
    return templates.TemplateResponse(
            "base.html",
            {"request": request},
            block_name="content"
            )
