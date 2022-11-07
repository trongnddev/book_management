from fastapi import FastAPI
from server.routes.book import router as book_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Book management app!"}

app.include_router(book_router, tags=["book"], prefix="/books")
