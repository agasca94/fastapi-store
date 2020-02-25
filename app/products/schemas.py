# from typing import Optional
from pydantic import BaseModel


class Department(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
