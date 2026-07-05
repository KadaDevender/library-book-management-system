from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from schemas.issued_book_schema import (
    IssueBookCreate,
    IssueBookResponse,
    IssueBookUpdate
)

import crud.issued_book_crud as crud

router = APIRouter(
    prefix="/issued-books",
    tags=["Issued Books"]
)


@router.post("/", response_model=IssueBookResponse)
def issue_book(
    issue: IssueBookCreate,
    db: Session = Depends(get_db)
):
    result = crud.issue_book(
        db,
        issue
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    if result == "NO_COPIES":
        raise HTTPException(
            status_code=400,
            detail="No Copies Available"
        )

    return result


@router.get("/", response_model=list[IssueBookResponse])
def get_issued_books(
    db: Session = Depends(get_db)
):
    return crud.get_issued_books(db)


@router.get("/{issue_id}", response_model=IssueBookResponse)
def get_issued_book(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = crud.get_issued_book(
        db,
        issue_id
    )

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue Record Not Found"
        )

    return issue


@router.put("/{issue_id}", response_model=IssueBookResponse)
def update_issued_book(
    issue_id: int,
    issue: IssueBookCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_issued_book(
        db,
        issue_id,
        issue
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Issue Record Not Found"
        )

    return updated


@router.patch("/{issue_id}", response_model=IssueBookResponse)
def patch_issued_book(
    issue_id: int,
    issue: IssueBookUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.patch_issued_book(
        db,
        issue_id,
        issue
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Issue Record Not Found"
        )

    return updated


@router.post("/return/{issue_id}")
def return_book(
    issue_id: int,
    db: Session = Depends(get_db)
):
    returned = crud.return_book(
        db,
        issue_id
    )

    if not returned:
        raise HTTPException(
            status_code=404,
            detail="Issue Record Not Found"
        )

    return {
        "message": "Book Returned Successfully"
    }


@router.delete("/{issue_id}")
def delete_issued_book(
    issue_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_issued_book(
        db,
        issue_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Issue Record Not Found"
        )

    return {
        "message": "Issue Record Deleted Successfully"
    }