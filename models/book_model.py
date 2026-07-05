from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):

    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    book_code = Column(String(50), unique=True)

    book_title = Column(String(255))
    author_name = Column(String(255))
    category = Column(String(100))
    publisher_name = Column(String(255))
    published_year = Column(Integer)
    total_copies = Column(Integer)
    available_copies = Column(Integer)
    shelf_location = Column(String(100))
    book_status = Column(String(50))


