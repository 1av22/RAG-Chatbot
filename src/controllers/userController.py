from fastapi import APIRouter

user_router = APIRouter()

user_router.prefix = "/user"

# route to create a new user


@user_router.post("/create")
def create_user():
    pass
