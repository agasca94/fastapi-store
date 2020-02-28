from typing import Optional
from datetime import date
from pydantic import BaseModel


class Customer(BaseModel):
    id: int = None
    name: str
    last_name: str
    email: str
    phone_number: str
    date_of_birth: date
    favorite_address_id: Optional[int]

    class Config:
        orm_mode = True


class CustomerCreate(Customer):
    password: str


class Address(BaseModel):
    id: int = None
    country: str
    state: str
    city: str
    zip_code: str
    street_number: str
    street_name: str
    phone_number: str
    extra_details: Optional[str]

    class Config:
        orm_mode = True
