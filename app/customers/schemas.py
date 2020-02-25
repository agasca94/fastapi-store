# from typing import Optional
from pydantic import BaseModel


class Address(BaseModel):
    id: int = None
    street_name: str
