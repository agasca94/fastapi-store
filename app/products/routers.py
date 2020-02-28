from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.utils import get_db
from app.products.repositories import department_repo, product_repo
from app.products.schemas import Department, Product, Review


departments_router = APIRouter()
products_router = APIRouter()
reviews_router = APIRouter()


# Departments controllers
@departments_router.get('/', response_model=List[Department])
def read_departments(db: Session = Depends(get_db)):
    departments = department_repo.get_paginated(db)
    return departments


@departments_router.get(
    '/{department_id}/products', response_model=List[Product]
)
def read_products_from_departments(
    department_id: int, db: Session = Depends(get_db)
):
    products = department_repo.get_products(db, department_id)
    return products


@departments_router.post('/', response_model=Department)
def create_department(db: Session = Depends(get_db)):
    return {'id': 1}


@departments_router.put('/{department_id}')
def update_department(department_id: int):
    return {'id': department_id}


@departments_router.delete('/{department_id}')
def delete_department(department_id: int):
    return {'deleted': department_id}


# Products controllers
@products_router.get('/', response_model=List[Product])
def read_products(db: Session = Depends(get_db)):
    products = product_repo.get_paginated(db)
    return products


@products_router.get('/{product_id}', response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_repo.get(db, product_id)
    return product


@products_router.post('/')
def create_product():
    return {'id': 1}


@products_router.put('/{product_id}')
def update_product(product_id: int):
    return {'id': product_id}


@products_router.delete('/{product_id}')
def delete_product(product_id: int):
    return {'deleted': product_id}


# Reviews controllers
@reviews_router.get('/', response_model=List[Review])
def read_reviews(product_id: int, db: Session = Depends(get_db)):
    reviews = product_repo.get_reviews(db, product_id)
    return reviews


@reviews_router.post('/')
def create_review(product_id: int):
    return {'id': 1}


@reviews_router.put('/')
def update_review(product_id: int):
    return {'id': 1}


@reviews_router.delete('/')
def delete_review(product_id: int):
    return {'deleted': 1}


router = APIRouter()
router.include_router(
    products_router,
    prefix='/products'
)
router.include_router(
    departments_router,
    prefix='/departments'
)
router.include_router(
    reviews_router,
    prefix='/products/{product_id}/reviews'
)
