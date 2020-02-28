from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.utils import get_db
from app.customers.repositories import customer_repo, address_repo
from app.customers.schemas import Address
from app.customers.models import Customer
from app.core.utils import get_current_user


address_router = APIRouter()

# Address controllers
@address_router.get('/', response_model=List[Address])
def read_addresses(
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user)
):
    address = customer_repo.get_addresses(db, current_user.id)
    return address


@address_router.post('/', response_model=Address)
def create_address(
    data: Address,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user),
):
    address = address_repo.create(db, obj=data, customer_id=current_user.id)
    return address


@address_router.put('/{address_id}')
def update_address(
    address_id: int,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user)
):
    return {'id': address_id}


@address_router.delete('/{address_id}')
def delete_address(
    address_id: int,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user)
):
    address_repo.remove(db, address_id)
    return {
        'deleted': address_id
    }


@address_router.post('/{address_id}/favorite')
def favorite_address(
    address_id: int,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user)
):
    return {'id': address_id}


router = APIRouter()
router.include_router(
    address_router,
    prefix='/me/addresses'
)
