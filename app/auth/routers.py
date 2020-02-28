from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.schemas import Token
from app.core.utils import get_db
from app.customers.repositories import customer_repo
from app.customers.schemas import CustomerCreate
from app.core.jwt import create_access_token


router = APIRouter()


@router.post('/login', response_model=Token)
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    customer = customer_repo.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not customer:
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )
    payload = {'customer_id': customer.id}
    access_token = create_access_token(data=payload)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }


@router.post('/register', response_model=Token)
def register(
    *,
    db: Session = Depends(get_db),
    data: CustomerCreate
):
    customer = customer_repo.get_by_email(db, data.email)
    if customer:
        raise HTTPException(
            status_code=400,
            detail='A user with this email already exists'
        )
    customer = customer_repo.create(db, obj=data)

    payload = {'customer_id': customer.id}
    access_token = create_access_token(data=payload)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }
