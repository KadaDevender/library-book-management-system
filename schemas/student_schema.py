from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    student_id: str
    student_name: str
    department: str
    year_of_study: int
    mobile_number: str


class StudentResponse(StudentCreate):

    class Config:
        from_attributes = True


class StudentUpdate(BaseModel):

    student_name: Optional[str] = None
    department: Optional[str] = None
    year_of_study: Optional[int] = None
    mobile_number: Optional[str] = None
