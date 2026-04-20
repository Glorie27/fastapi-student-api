from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app =   FastAPI()

students = []
class Student(BaseModel):
    id: int
    name: str
    department: int
    level: Optional[str] = None

@app.get("/")
def home ():
    return {"message": "Welcome to the Student API"}

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student created successfully", "student": student}

@app.get("/students")
def get_students():
    return {"students": students}

