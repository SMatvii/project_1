from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from app.db import Books
from app import app
import re

book_db = []

class Book(BaseModel):
    title: str = Field(..., title="Назва книги")
    author: str = Field(..., title="Автор книги")
    year: int = Field(..., ge=0, title="Рік видання")
    genre: str = Field(..., title="Жанр")
    isbn: str = Field(..., title="ISBN", description="ISBN повинен містити 13 цифр")

    @validator('isbn')
    def validate_isbn(cls, isbn: str) -> str:
        if not re.fullmatch(r"\d{13}", isbn):
            raise ValueError("ISBN повинен містити рівно 13 цифр")
        return isbn

@app.post("/books/")
async def create_book(book: Book):
    if book.isbn in book_db:
        raise HTTPException(status_code=400, detail="ISBN має бути унікальним")
    
    book_db.append(book.isbn)
    return {"message": "Книга успішно додана", "book": book}