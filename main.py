<<<<<<< HEAD
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

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return {"student": student}
    return {"message": "Student not found"}

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student updated successfully", "student": updated_student}
    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted successfully"}
    return {"message": "Student not found"}
=======
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

>>>>>>> 227fe1d5625ba1d875a71388af24c18b09b75483
