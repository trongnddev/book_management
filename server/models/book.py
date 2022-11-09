from typing import Union, List, overload
from umongo import Document, fields
import asyncio
from datetime import datetime
from bson import ObjectId
from fastapi import status

from config.config_database import  instance
from ..models.author import Author
from ..schemas.book import BookSchemas



@instance.register
class Book(Document):
    # book_id = fields.StringField(reqiured=True)
    name = fields.StringField(required=True)
    description = fields.StringField()
    price = fields.FloatField(required=True)
    author_id = fields.ObjectIdField(required=True)
    created_date = fields.DateTimeField()
    updated_date = fields.DateField()
    type = fields.StringField()
    

    
    def pre_insert(self):
        self.created_date = datetime.now()
        self.updated_date  = datetime.now()
        self.name = self.name.strip().upper()
        
        
    class Meta:
        collection_name = "books"

async def get_all():

    books = await Book.find().to_list(None)
    list_books = []
    for i in books:
        list_books.append(i.dump())
    result = {"Code error":"",
              "Message success":"",
              "Data": list_books}
    return result
    
async def create(book:BookSchemas):
    check_book = await Book.find_one({"author_id":ObjectId(book.author_id), "name":book.name})
    result = {  "Code error": "",
                "Message success":"",
                "Data": ""
            }
    if check_book:
        result["Code error"]= "sách đã có trong hệ thống"
        return result
    new_book =  Book()
    new_book.name = book.name
    new_book.description = book.description
    new_book.author_id = book.author_id
    new_book.price= book.price
    new_book.type = book.type
    await new_book.commit()
    
    result["Message success"] = "Đã tạo book thành công"
    result["Data"] = new_book.dump()
    return result    

async def get_book_by_author_id(author: dict):
    """
    param:  {
        "id": "str"
    }
    """
    list_book = await Book.find({"author_id": ObjectId(author['id'])}).to_list(None)
    print(list_book)
    books = []
    for b in list_book:
        books.append(b.dump())
    result = {"Code error":"",
              "Message success":"",
              "Data": books}
    return result

async def get_book(input: dict):
    pipline = [
        {
            '$match': { 'name': {'$regex': input.get('name'), '$options': 'i'},
                        'description': {'$regex': input.get('description'), '$options': 'i'}}
        }
    ]
    books =  Book.collection.aggregate(pipline)
    result = {
        "Error code": "",
        "Mesage success": "",
        "Data": {}
    }
    if books:
        list_book = []
        
        async for b in books:
            author = await Author.collection.find_one({"_id": b.get('author_id')})
            value = {
                "name" : b.get("name"),
                "description": b.get("description"),
                "created_date": b.get("created_date"),
                "updated_date": b.get("updated_date"),
                "author": author.get("name")
            }           
            list_book.append(value)
        result['Data']['count'] = len(list_book)
        result['Data']['body'] = list_book
        result["Error code"] = status.HTTP_200_OK

        return result
    else:
        result['Mesage success'] = 'Không tìm thấy sách!'
        result['Error code'] = status.HTTP_404_NOT_FOUND
        return result

    