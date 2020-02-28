from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.repositories import CRUDRepository
from app.customers import schemas, models
from app.core.security import verify_password, hash_password


class AddressRepository(
    CRUDRepository[models.Address, schemas.Address, schemas.Address]
):
    pass


class CustomerRepository(
    CRUDRepository[models.Customer, schemas.CustomerCreate, schemas.Customer]
):
    def get_by_email(
        self, sess: Session, email: str
    ) -> Optional[models.Customer]:
        return sess.query(models.Customer).filter_by(email=email).first()

    def create(
        self, sess: Session, obj: schemas.CustomerCreate
    ) -> models.Customer:
        data = obj.dict()
        data['password'] = hash_password(data['password'])
        instance = models.Customer(**data)
        sess.add(instance)
        sess.commit()
        sess.refresh(instance)

        return instance

    def authenticate(
        self, sess: Session, *, email: str, password: str
    ) -> Optional[models.Customer]:
        customer = self.get_by_email(sess, email)
        if not customer:
            return None
        if not verify_password(password, customer.password):
            return None
        return customer

    def get_addresses(self, sess: Session, _id: int) -> List[models.Address]:
        customer = self.get(sess, _id)
        return customer.addresses


customer_repo = CustomerRepository(models.Customer)
address_repo = AddressRepository(models.Address)
