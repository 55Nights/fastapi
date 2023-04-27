from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from .import models, schemas
from .database import get_db
from . import schemas
from .config import settings
oauth_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    # data is payload to be added to the token function
    data_to_encode = data.copy()
    exp = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # add exp to payload
    data_to_encode.update({"exp": exp})

    token = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_access_token(token: str, cred_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_ID")

        if id is None:
            raise cred_exception
        tken = schemas.TokenPayLoad(id=id)
    except JWTError:
        raise cred_exception

    return payload


def get_current_user(
        token: str = Depends(oauth_schema),
        db: Session = Depends(get_db)):
    cred_excepton = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate user",
        headers={
            "WWW-Authenticate": "Bearer"})
    token_id = verify_access_token(token, cred_excepton)
    print(token_id)
    print(token)
    user = db.query(
        models.Users).filter(
        models.Users.id == token_id['user_ID']).first()

    return user
