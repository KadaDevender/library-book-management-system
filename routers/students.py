from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.student_schema import (
    StudentCreate,
    StudentResponse,
    StudentUpdate
)

import crud.student_crud as crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: str,
    db: Session = Depends(get_db)
):
    student = crud.get_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: str,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_student(
        db,
        student_id,
        student
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return updated


@router.patch("/{student_id}", response_model=StudentResponse)
def patch_student(
    student_id: str,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.patch_student(
        db,
        student_id,
        student
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return updated


@router.delete("/{student_id}")
def delete_student(
    student_id: str,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_student(
        db,
        student_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return {
        "message": "Student Deleted Successfully"
    }