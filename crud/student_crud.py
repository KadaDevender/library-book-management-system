from sqlalchemy.orm import Session
from models.student_model import Student


def create_student(db: Session, student):
    db_student = Student(**student.dict())

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(Student).all()



def get_student(db: Session, student_id: str):
    return (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )



def update_student(
    db: Session,
    student_id: str,
    student
):
    db_student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if db_student:
        for key, value in student.dict().items():
            setattr(db_student, key, value)

        db.commit()
        db.refresh(db_student)

    return db_student



def patch_student(
    db: Session,
    student_id: str,
    student
):
    db_student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not db_student:
        return None

    update_data = student.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student



def delete_student(
    db: Session,
    student_id: str
):
    db_student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if db_student:
        db.delete(db_student)
        db.commit()

    return db_student