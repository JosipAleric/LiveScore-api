from fastapi import APIRouter, Depends
from controllers import AuthController
from pydantic import BaseModel, Field, EmailStr

from controllers.AuthController import get_current_user, oauth2_scheme

router = APIRouter()

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=4)
    email: EmailStr
    first_name: str = Field(..., min_length=2, max_length=20)
    last_name: str = Field(..., min_length=2, max_length=20)
    is_admin: int

class UserDetails(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    is_admin: int
class UserLogin(BaseModel):
    email: str
    password: str


@router.get("/")
async def get_users():
    users = AuthController.get_users()
    return users


@router.post("/register")
async def register_user(user: User):
    return AuthController.register_user(user)


@router.post("/login")
async def login(request: UserLogin):
    return AuthController.login(request)


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    return AuthController.logout(token)


# @router.get("/get_current_user")
# async def get_logged_user(access_token: str):
#     return AuthController.get_current_user(access_token)


# @router.get("/users/get_current_user", dependencies=[Depends(get_current_user)])
# async def get_current_user(current_user: User):
#     """Retrieves the currently logged-in user."""
#     return current_user

@router.get("/get_current_user", dependencies=[Depends(get_current_user)])
async def get_current_user(current_user: UserDetails = Depends(get_current_user)):
    return current_user
