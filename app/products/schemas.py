# from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class Department(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: int
    name: str
    description: str
    stock: int
    price: float
    department: Department

    class Config:
        orm_mode = True


class Review(BaseModel):
    id: int
    score: int
    description: str
    created_at: datetime
    customer_id: int

    class Config:
        orm_mode = True
