from fastapi import FastAPI

from .src.controllers.userController import user_router
from .src.utils.database import initialize_database
from .src.utils.database import initialize_database

app = FastAPI()
app.include_router(user_router)
initialize_database()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}
