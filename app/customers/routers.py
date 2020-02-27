from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.utils import get_db
from app.customers.repositories import customer_repo
from app.customers.schemas import Address


address_router = APIRouter()

# Address controllers
@address_router.get('/', response_model=List[Address])
def read_addresses(
    customer_id: int,
    db: Session = Depends(get_db)
):
    address = customer_repo.get_addresses(db, customer_id)

    return address


@address_router.post('/')
def create_address(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return {'id': 1}


@address_router.put('/{address_id}')
def update_address(
    customer_id: int,
    address_id: int,
    db: Session = Depends(get_db)
):
    return {'id': address_id}


@address_router.delete('/{address_id}')
def delete_address(
    customer_id: int,
    address_id: int,
    db: Session = Depends(get_db)
):
    return {'id': address_id}


@address_router.post('/{address_id}/favorite')
def favorite_address(
    customer_id: int,
    address_id: int,
    db: Session = Depends(get_db)
):
    return {'id': address_id}


router = APIRouter()
router.include_router(
    address_router,
    prefix='/customers/{customer_id}/addresses'
)
