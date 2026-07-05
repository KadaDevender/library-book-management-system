from sqlalchemy import Column, String, Integer
from models.book_model import Base


class Student(Base):

    __tablename__ = "students"

    student_id = Column( String(20), primary_key=True, index=True )
    student_name = Column(String(100),nullable=False)
    department = Column( String(50),nullable=False)
    year_of_study = Column(Integer,nullable=False)
    mobile_number = Column(String(15),nullable=False)

    