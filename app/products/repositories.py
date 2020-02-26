from typing import List
from app.core.repositories import CRUDRepository
from app.products import schemas, models
from sqlalchemy.orm import Session


class DepartmentRepository(
    CRUDRepository[models.Department, schemas.Department, schemas.Department]
):
    def get_products(self, sess: Session, _id: int) -> List[models.Product]:
        department = self.get(sess, _id)
        return department.products


class ProductRepository(
    CRUDRepository[models.Product, schemas.Product, schemas.Product]
):
    def get_reviews(self, sess: Session, _id: int) -> List[models.Review]:
        product = self.get(sess, _id)
        return product.reviews


department_repo = DepartmentRepository(models.Department)
product_repo = ProductRepository(models.Product)
