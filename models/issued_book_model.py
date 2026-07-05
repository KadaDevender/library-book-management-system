from sqlalchemy import (Column,Integer,String,Date,ForeignKey)
from models.book_model import Base


class IssuedBook(Base):

    __tablename__ = "issued_books"
    
    issue_id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("books.id"),nullable=False)
    student_id = Column(String(20),ForeignKey("students.student_id"),nullable=False)
    student_name = Column(String(100),nullable=False)
    issue_date = Column(Date,nullable=False)
    due_date = Column(Date,nullable=False)
    return_date = Column(Date,nullable=True)
    issue_status = Column(String(20), default="ISSUED")