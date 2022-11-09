from http.client import HTTPResponse
from umongo import Document, fields
from bson.objectid import ObjectId

from config.config_database import instance
from ..schemas.author import AuthorSchemas




@instance.register
class Author(Document):
    name = fields.StringField(required=True)
    phone = fields.StringField(required=True, unique=True)
    born_year = fields.IntegerField(required=True)
    # list_book = fi(Book,defaut=[],allow_none = True)

    class Meta:
        collection_name = "author"


 
async def get_all():
    authors = await Author.find().to_list(None)
    list_author = []
    for i in authors:
        list_author.append(i.dump())
    result = {"Code error":"",
              "Message success":"",
              "Data": list_author}
    return result

async def create(author: AuthorSchemas):
    check_phone = await Author.find_one({"phone":author.phone})
    result = {  "Code error": "",
                "Message success":"",
                "Data": ""
            }
    if check_phone:
        result["Code error"]= "Phone đã có trong hệ thống"
        return result
    new_author =  Author()
    new_author.name = author.name
    new_author.born_year = author.born_year
    new_author.phone= author.phone
   
    await new_author.commit()
    result["Message success"] = "Đã tạo author thành công"
    result["Data"] = new_author.dump()
    return result

async def get_one(name: str):
    author : Author = await Author.collection.find_one({"name":name})
    if not author:
        return "Khong co"
    value = {
        "name": author.get("name"),
        "phone": author.get("phone"),
        "born_year": author.get("born_year")
    }
    result = {"Code error":"",
              "Message success":"",
              "Data": value}
    return result


async def delete(author: AuthorSchemas):
    au : Author = await Author.find_one(
        {"phone":author.phone
           })
    result = {"Code error":"",
              "Message success":"",
              "Data": ""}
    if au:
        await au.delete()
        result["Message success"]= "Delete success"
    else:
        result["Code error"]= "Don't find author"
    return result

async def update(values: dict):
    author = await Author.find_one({"name":values["name"],
            "phone":values["phone"]})
    result = {"Code error": "",
                "Message success":"",
                "Data": ""}        
    if not author:
        result["Code error"] = "Không tìm thấy author"
        return result
    else:
        if values.get("new_phone"):
            if values["new_phone"] != author.phone:
                if await Author.find_one({"phone":values["new_phone"]}):
                    result["Message success"] = "sdt đã được gán cho một author khác!"
                    return result
                author.phone = values["new_phone"]
        if values.get("new_name"):
            author.name = values["new_name"]
        if values.get("new_born_year"):
            author.born_year = values["new_born_year"] 
        await author.commit()
        result = {"Code error":"",
              "Message success":"Update author thành công",
              "Data": author.dump()}
        return result
    
        
    
