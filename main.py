from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from api import routes

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(routes.router)

openapi_schema = get_openapi(
    title="Documents API",
    version="0.1.0",
    description="API for storing and retriving documents in json.",
    routes=app.routes,
)
# import json
# with open("openapi.yaml", "w") as file:
# file.write(json.dumps(openapi_schema))


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "documents api @bhunao"}
