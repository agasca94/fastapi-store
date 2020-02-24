from fastapi import APIRouter

departments_router = APIRouter()
products_router = APIRouter()
reviews_router = APIRouter()


# Departments controllers
@departments_router.get('/')
def read_departments():
    return [{'id': 1}, {'id': 2}, {'id': 3}]


@departments_router.get('/{department_id}/products')
def read_products_from_departments(department_id: int):
    return [{'id': 1}, {'id': 2}, {'id': 3}]


@departments_router.put('/{department_id}')
def get_department(department_id: int):
    return {'id': department_id}


@departments_router.post('/')
def create_department():
    return {'id': 1}


@departments_router.put('/{department_id}')
def update_department(department_id: int):
    return {'id': department_id}


@departments_router.delete('/{department_id}')
def delete_department(department_id: int):
    return {'deleted': department_id}


# Products controllers
@products_router.get('/')
def read_products():
    return [{'id': 1}, {'id': 2}, {'id': 3}]


@products_router.put('/{product_id}')
def get_product(product_id: int):
    return {'id': product_id}


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
@reviews_router.get('/')
def read_reviews(product_id: int):
    return [{'id': 1}, {'id': 2}, {'id': 3}]


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
