from fastapi import FastAPI
from .routes.book import router as book_router
from .routes.author import router as author_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Book management app!"}

app.include_router(author_router, tags=["author"], prefix="/authors")
app.include_router(book_router, tags=["book"], prefix="/books")
