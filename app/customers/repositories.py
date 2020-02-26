from sqlalchemy.orm import Session
from typing import List
from app.core.repositories import CRUDRepository
from app.customers import schemas, models


class AddressRepository(
    CRUDRepository[models.Address, schemas.Address, schemas.Address]
):
    pass


class CustomerRepository(
    CRUDRepository[models.Customer, schemas.Customer, schemas.Customer]
):
    def get_addresses(self, sess: Session, _id: int) -> List[models.Address]:
        customer = self.get(sess, _id)
        return customer.addresses


customer_repo = CustomerRepository(models.Customer)
