from sqlalchemy.orm import Session

from models.issued_book_model import IssuedBook
from models.book_model import Book


# ISSUE BOOK
def issue_book(
    db: Session,
    issue
):
    book = (
        db.query(Book)
        .filter(Book.id == issue.book_id)
        .first()
    )

    if not book:
        return None

    if book.available_copies <= 0:
        return "NO_COPIES"

    db_issue = IssuedBook(**issue.dict())

    db.add(db_issue)

    book.available_copies -= 1

    db.commit()
    db.refresh(db_issue)

    return db_issue


# GET ALL ISSUED BOOKS
def get_issued_books(db: Session):
    return db.query(IssuedBook).all()


# GET ISSUED BOOK BY ID
def get_issued_book(
    db: Session,
    issue_id: int
):
    return (
        db.query(IssuedBook)
        .filter(IssuedBook.issue_id == issue_id)
        .first()
    )


# UPDATE ISSUED BOOK (PUT)
def update_issued_book(
    db: Session,
    issue_id: int,
    issue
):
    db_issue = (
        db.query(IssuedBook)
        .filter(IssuedBook.issue_id == issue_id)
        .first()
    )

    if db_issue:
        for key, value in issue.dict().items():
            setattr(db_issue, key, value)

        db.commit()
        db.refresh(db_issue)

    return db_issue


# PATCH ISSUED BOOK
def patch_issued_book(
    db: Session,
    issue_id: int,
    issue
):
    db_issue = (
        db.query(IssuedBook)
        .filter(IssuedBook.issue_id == issue_id)
        .first()
    )

    if not db_issue:
        return None

    update_data = issue.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_issue, key, value)

    db.commit()
    db.refresh(db_issue)

    return db_issue


# RETURN BOOK
def return_book(
    db: Session,
    issue_id: int
):
    db_issue = (
        db.query(IssuedBook)
        .filter(IssuedBook.issue_id == issue_id)
        .first()
    )

    if not db_issue:
        return None

    book = (
        db.query(Book)
        .filter(Book.id == db_issue.book_id)
        .first()
    )

    if book:
        book.available_copies += 1

    db_issue.issue_status = "RETURNED"

    db.commit()
    db.refresh(db_issue)

    return db_issue


# DELETE ISSUE RECORD
def delete_issued_book(
    db: Session,
    issue_id: int
):
    db_issue = (
        db.query(IssuedBook)
        .filter(IssuedBook.issue_id == issue_id)
        .first()
    )

    if db_issue:
        db.delete(db_issue)
        db.commit()

    return db_issue