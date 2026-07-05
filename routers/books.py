from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.book_schema import BookCreate,BookUpdate
import crud.book_crud as book_crud

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/")
def create_book(book:BookCreate,db:Session=Depends(get_db)):
    return book_crud.create_book(db,book)


@router.get("/")
def get_books(db:Session=Depends(get_db)):
    return book_crud.get_books(db)


@router.get("/{book_id}")
def get_book(book_id:int,db:Session=Depends(get_db)):
    book = book_crud.get_book(db,book_id)
    if not book:
        raise HTTPException(status_code=404,detail="Book Not Found")
    return book


@router.put("/{book_id}")
def update_book(book_id:int,book:BookCreate,db:Session=Depends(get_db)):
    updated = book_crud.update_book(db,book_id,book)
    if not updated:
        raise HTTPException(status_code=404,detail="Book Not Found")
    return updated


@router.patch("/{book_id}")
def patch_book(book_id: int,book: BookUpdate,db: Session = Depends(get_db)):
    updated = book_crud.patch_book(db,book_id,book)
    if not updated:
        raise HTTPException(status_code=404,detail="Book Not Found")
    return updated


@router.delete("/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    deleted = book_crud.delete_book( db,book_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Book Not Found")
    return {"message":"Book Deleted Successfully"}


    
