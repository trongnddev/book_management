from pydantic import BaseModel, Field,fields,validator
from .book import BookSchemas
from typing import List
import datetime


class AuthorSchemas(BaseModel):
    name : str = Field (title="Author's name", max_length=150)
    born_year : int = Field (title="Author's old", lt=2004 )
    phone: str = Field (title="Author's phone", max_length=11, min_length=10)

    # @validator('name')
    # def check_name(cls,v):
    #     for char in v:
    #         if not char.isalpha():
    #             return "name không hợp lệ"
    #     return v

    # @validator('born_year')
    # def check_year(cls,v):
    #     if v - datetime.date.today().year < 18:
    #         return ValueError ("date_born ")
    #     return v


class FindOne(BaseModel):
    name : str
