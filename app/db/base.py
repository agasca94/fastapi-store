# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base # noqa
from app.customers import models  # noqa
from app.products import models # noqa
