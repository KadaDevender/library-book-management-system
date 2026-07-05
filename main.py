from fastapi import FastAPI

from routers.books import router as book_router
from routers.students import router as student_router
from routers.issued_books import router as issued_router

app = FastAPI(
    title="Library Management System API"
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Library Management System API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

app.include_router(book_router)
app.include_router(student_router)
app.include_router(issued_router)
