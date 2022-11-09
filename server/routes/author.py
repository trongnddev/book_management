from fastapi import APIRouter, status

from ..models.author import get_all, Author, create, get_one, delete, update
from ..schemas.author import AuthorSchemas,FindOne
    
router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def get_authors():
    return await get_all()


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_author(author: AuthorSchemas):
    return await create(author=author)



@router.post('/find_author')
async def find_author(data: FindOne):
    a = await get_one(data.name)
    return a

@router.post('/delete', status_code=status.HTTP_200_OK)
async def delete_author(author: AuthorSchemas   ):
    return await delete(author)


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_author(values: dict):
    return await update(values=values)