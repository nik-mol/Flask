
from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from typing import Type
from errors import HttpExeption


class AdvertisementSchema(BaseModel):

    title: str=Field(min_length=3, max_length=15) 
    description: str=Field(min_length=10, max_length=50) 
    owner: str=Field(min_length=5, max_length=20) 


        
def validate(data_to_validate: dict, validation_model: Type[AdvertisementSchema]):
    try:
        return validation_model(**data_to_validate).dict(exclude_none=True) 
    except ValidationError as er:
        raise HttpExeption(400, er.errors())



