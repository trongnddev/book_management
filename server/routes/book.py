from fastapi import APIRouter, Body, status
from  server.models.book import Book
router = APIRouter()





fake_books_db = [
    {"book_name": "Nhà giả kim"},
    {"book_name": "Đắc nhân tâm"}, 
    {"book_name": "Trên Đường Băng"},
    {"book_name": "Cha giàu, cha nghèo"},
    {"book_name": "Tuổi trẻ đáng giá bao nhiêu"},
    {"book_name": "Thao túng tâm lý"},
    {"book_name": "Tuổi trẻ đáng giá bao nhiêu"},
    {"book_name": "Đừng lựa chọn an nhàn khi còn trẻ"},
    {"book_name":"Khéo ăn khéo nói sẽ có được thiên hạ"},
    {"book_name": "Mỗi lần vấp ngã là một lần trưởng thành"},
    {"book_name": "Đời ngắn đừng ngủ dài"},
    {"book_name": "Tôi giỏi bạn cũng thế"},
    
    ]


# path parameter
# Get 1
@router.get("/{book_id}")
async def get_one(book_id: int):
    return fake_books_db[book_id]


# Query parameter 
# Get all
@router.get("/", status_code=status.HTTP_200_OK)
async def read_item(skip: int = 0, limit: int = 5):
    return fake_books_db[skip : skip + limit]

#create
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(book: Book):
    return book 