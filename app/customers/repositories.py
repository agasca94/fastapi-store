from app.core.repositories import CRUDRepository
from app.customers import schemas, models


class AddressRepository(
    CRUDRepository[models.Address, schemas.Address, schemas.Address]
):
    pass


address_repo = AddressRepository(models.Address)
