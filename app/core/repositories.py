from typing import List, Optional, Generic, TypeVar, Type
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.db.base_class import Base


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, sess: Session, id: int) -> Optional[ModelType]:
        return sess.query(self.model).filter(self.model.id == id).first()

    def get_paginated(
        self, sess: Session, *, page=None, page_size=20
    ) -> List[ModelType]:
        if page is not None:
            skip = page - 1
            limit = page_size
            return sess.query(self.model).offset(skip).limit(limit).all()

        return sess.query(self.model).all()

    def create(self, sess: Session, *, obj: CreateSchemaType) -> ModelType:
        data = jsonable_encoder(obj)
        instance = self.model(**data)
        sess.add(instance)
        sess.commit()
        sess.refresh(instance)

        return instance

    def update(
        self, sess: Session, *, instance: ModelType, obj: UpdateSchemaType
    ) -> ModelType:
        data = jsonable_encoder(instance)
        update_data = obj.dict(skip_defaults=True)
        for field in data:
            if field in update_data:
                setattr(instance, field, update_data[field])

        sess.add(instance)
        sess.commit()
        sess.refresh(instance)

        return instance

    def remove(self, sess: Session, *, _id: int) -> ModelType:
        instance = sess.query(self.model).get(_id)
        sess.delete(instance)
        sess.commit()

        return instance
