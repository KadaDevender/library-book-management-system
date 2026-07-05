# Library Book Management System

A RESTful Library Management System built using FastAPI, SQLAlchemy, and MySQL.

## Features

* Book Management (CRUD)
* Student Management (CRUD)
* Issue Books to Students
* Return Books
* Automatic Available Copies Update
* PATCH Support
* MySQL Database Integration
* Swagger API Documentation

## Tech Stack

* FastAPI
* Python
* SQLAlchemy ORM
* MySQL
* Pydantic
* Uvicorn

## Project Structure

```text
Library_Book_Management_System/

├── database.py
├── main.py

├── models/
│   ├── book_model.py
│   ├── student_model.py
│   └── issued_book_model.py

├── schemas/
│   ├── book_schema.py
│   ├── student_schema.py
│   └── issued_book_schema.py

├── crud/
│   ├── book_crud.py
│   ├── student_crud.py
│   └── issued_book_crud.py

├── routers/
│   ├── books.py
│   ├── students.py
│   └── issued_books.py
```

## Database Tables

### books

* id
* book_code
* book_title
* author_name
* category
* publisher_name
* published_year
* total_copies
* available_copies
* shelf_location
* book_status

### students

* student_id
* student_name
* department
* year_of_study
* mobile_number

### issued_books

* issue_id
* book_id
* student_id
* student_name
* issue_date
* due_date
* return_date
* issue_status

## API Endpoints

### Books

| Method | Endpoint    |
| ------ | ----------- |
| POST   | /books      |
| GET    | /books      |
| GET    | /books/{id} |
| PUT    | /books/{id} |
| PATCH  | /books/{id} |
| DELETE | /books/{id} |

### Students

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /students              |
| GET    | /students              |
| GET    | /students/{student_id} |
| PUT    | /students/{student_id} |
| PATCH  | /students/{student_id} |
| DELETE | /students/{student_id} |

### Issued Books

| Method | Endpoint                        |
| ------ | ------------------------------- |
| POST   | /issued-books                   |
| GET    | /issued-books                   |
| GET    | /issued-books/{issue_id}        |
| PUT    | /issued-books/{issue_id}        |
| PATCH  | /issued-books/{issue_id}        |
| POST   | /issued-books/return/{issue_id} |
| DELETE | /issued-books/{issue_id}        |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Author

Devender Kada
