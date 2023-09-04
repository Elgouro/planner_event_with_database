from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])

users = {}

@user_router.post('/signup')
async def sign_new_user(data: User )->dict:
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="you have already been signedIn let try connect you ")
    users[data.email]= data
    return {
        "message":"User successfully registred!"
    }

@user_router.post("/signin")
async def sign_in(userauth: UserSignIn)->dict:
    if userauth.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found please create an account")
    stored_user = users[userauth.email]
    if stored_user.password != userauth.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="wrong credentials please passed enter the right one")
    return{
        "message":"user signed in successfully"
    }