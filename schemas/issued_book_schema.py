from pydantic import BaseModel
from datetime import date
from typing import Optional


class IssueBookCreate(BaseModel):

    book_id: int
    student_id: str
    student_name: str
    issue_date: date
    due_date: date


class IssueBookResponse(IssueBookCreate):

    issue_id: int
    return_date: Optional[date] = None
    issue_status: str

    class Config:
        from_attributes = True


class IssueBookUpdate(BaseModel):

    book_id: Optional[int] = None
    student_id: Optional[str] = None
    student_name: Optional[str] = None
    issue_date: Optional[date] = None
    due_date: Optional[date] = None
    return_date: Optional[date] = None
    issue_status: Optional[str] = None