from fastapi import APIRouter, status

from  ..models.book import Book, get_all, create, get_book_by_author_id, get_book
from ..schemas.book import BookSchemas

router = APIRouter()



@router.get('/', status_code=status.HTTP_200_OK)
async def get_books():
    return await get_all()


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_books(book: BookSchemas):
    return await create(book=book)

@router.post('/find_book_by_author_id',status_code=status.HTTP_200_OK)
async def find_book_by_author_id(author: dict):
    return await get_book_by_author_id(author=author)

@router.post('/find_book',status_code=status.HTTP_200_OK)
async def find_book(input: dict):
        return await get_book(input=input)