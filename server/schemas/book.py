from typing import Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class TypeEnum(str, Enum):
    tieuthuyet = "Tiểu Thuyết"
    tho = "Thơ"
    laptrinh = "Lập trình"
    vanhoc = "Văn học"
    daoduc = "Đạo đức"


class BookSchemas(BaseModel):
    name: str = Field (title="Book's name", max_length=300)
    description: Union[str, None] =  Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float  
    author_id: str
    type : TypeEnum
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Điền tên sách",
                "description": "mô tả",
                "price": 35.4,
                "author": "Nguyễn Văn A",
               
            }
        }


    