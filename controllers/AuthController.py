from sqlalchemy.exc import NoResultFound

from models.user import User, TokenTable
from models import db
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import utils
from datetime import datetime, timedelta
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def add_user(username, password, email, first_name, last_name):
    new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    db.add(new_user)
    db.commit()
    return new_user

def get_users():
    users = db.query(User).all()
    return users

def delete_user(user_id):
    user = db.query(User).get(user_id)
    db.delete(user)
    db.commit()
    return user

def update_user(user_id, username, password, email, first_name, last_name, is_admin):
    user = db.query(User).get(user_id)
    user.username = username
    user.password = password
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.is_admin = is_admin
    db.commit()
    return user

def get_user(user_id):
    user = db.query(User).get(user_id)
    return user


def register_user(user: User):
    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Korisnik s tim emailom već postoji")

    encrypted_password = utils.get_hashed_password(user.password)

    new_user = User(username=user.username, password=encrypted_password , email=user.email, first_name=user.first_name, last_name=user.last_name)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"Uspješna registracija", "data": new_user}


def login(request):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Netočan email")
    hashed_pass = user.password
    encrypted_password = utils.get_hashed_password(request.password)
    if not utils.verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Netočna lozinka"
        )

    access = utils.create_access_token(user.id)
    refresh = utils.create_refresh_token(user.id)

    token_db = TokenTable(user_id=user.id, access_token=access, refresh_token=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)

    return {
        "access_token": access,
        "user": user,
        "token_type": "bearer"
    }


# def logout(access_token: str):
#     token = db.query(TokenTable).filter(TokenTable.access_token == access_token).first()
#     if token is None:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nešto je pošlo krivo")
#
#     # delete token from db
#     db.delete(token)
#     db.commit()
#     return {"message": "Uspješna odjava"}

def logout(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, utils.JWT_SECRET_KEY, algorithms=[utils.ALGORITHM])
        user_id: int = payload.get("sub")
        if not user_id:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    try:
        # Query the database to get the user's tokens
        tokens = db.query(TokenTable).filter(TokenTable.user_id == user_id).all()

        # Delete the tokens from the database
        for token in tokens:
            db.delete(token)
        db.commit()

        return {"message": "Successfully logged out"}

    except NoResultFound:
        raise HTTPException(status_code=404, detail="No active tokens found for this user")


def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="login"))):
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User error",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        payload = jwt.decode(token, utils.JWT_SECRET_KEY, algorithms=[utils.ALGORITHM])
        print(payload)
        user_id: int = payload.get("sub")
        if not user_id:
             raise credentials_exception
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nešto je pošlo krivo")

    user = db.query(User).filter(User.id == user_id).first()
    response = {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_admin": user.is_admin,
    }

    return response
