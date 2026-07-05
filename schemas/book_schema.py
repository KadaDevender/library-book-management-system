from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    book_code:str
    book_title:str
    author_name:str
    category:str
    publisher_name:str
    published_year:int

    total_copies:int = Field(gt=0)
    available_copies:int = Field(ge=0)

    shelf_location:str
    book_status:str


class BookResponse(BookCreate):
    id:int

    class Config:
        from_attributes = True

class BookUpdate(BaseModel):

    book_code: Optional[str] = None
    book_title: Optional[str] = None
    author_name: Optional[str] = None
    category: Optional[str] = None
    publisher_name: Optional[str] = None
    published_year: Optional[int] = None

    total_copies: Optional[int] = None
    available_copies: Optional[int] = None

    shelf_location: Optional[str] = None
    book_status: Optional[str] = None

