from app.core.repositories import CRUDRepository
from app.products import schemas, models


class DepartmentRepository(
    CRUDRepository[models.Department, schemas.Department, schemas.Department]
):
    pass


department_repo = DepartmentRepository(models.Department)
