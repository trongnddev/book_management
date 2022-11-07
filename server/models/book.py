from pydantic import BaseModel,validator, Field, HttpUrl
from typing import Union, List


class Image(BaseModel):
    url: HttpUrl
    name: str

class Book(BaseModel):
    name: str = Field (title="Book's name", max_length=300)
    description: Union[str, None] =  Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float  
    author: str
    images: Union[List[Image], None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Điền tên sách",
                "description": "mô tả",
                "price": 35.4,
                "author": "Nguyễn Văn A",
                "images": [
                                {
                                    "url": "http://example.com/baz.jpg",
                                    "name": "The Foo live"
                                },
                                {
                                    "url": "http://example.com/dave.jpg",
                                    "name": "The Baz"
                                }
                            ] 
            }
        }
   