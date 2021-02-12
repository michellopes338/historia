from abc import ABC
from typing import Generic, Optional, Type, TypeVar, Any
from pydantic.main import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from ..connection import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABC):

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def create(self, database: Session, data: CreateSchemaType) -> ModelType:
        obj_db = self.model(**data.dict())

        database.add(obj_db)
        database.commit()
        database.refresh(obj_db)

        return obj_db
    
    def read(self, database: Session, id: Any) -> Optional[ModelType]:
        return database.query(self.model).filter_by(id=id).first()
    
    def update(
        self,
        database: Session,
        obj_db: ModelType,
        new_data: dict
    ) -> ModelType:
        
        old_data = jsonable_encoder(obj_db)

        for field in old_data:
            if field in new_data:
                setattr(obj_db, field, new_data[field])

        database.add(obj_db)
        database.commit()
        database.refresh(obj_db)

        return obj_db
    
    def delete(self, database: Session, id: int) -> ModelType:
        obj_db = database.query(self.model).filter_by(id=id).first()

        database.delete(obj_db)
        database.commit()

        return obj_db