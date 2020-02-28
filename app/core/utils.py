import jwt
from jwt import PyJWTError
from fastapi import Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette.requests import Request
from app.core import config
from app.core.jwt import ALGORITHM
from app.auth.schemas import TokenPayload
from app.customers.repositories import customer_repo
from starlette import status


def get_db(request: Request):
    return request.state.db


oauth2_scheme = OAuth2PasswordBearer('/login')


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Security(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            config.JWT_SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials'
        )
    user = customer_repo.get(db, token_data.customer_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )

    return user
