from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory database
students_db = []
student_id_counter = 1

class Student(BaseModel):
    Name: str
    Email: str
    age: int
    Roll_no: int
    Department: str

class StudentResponse(Student):
    id: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/students", response_model=StudentResponse)
def create_student_endpoint(student: Student):
    global student_id_counter
    new_student = StudentResponse(id=student_id_counter, **student.dict())
    students_db.append(new_student)
    student_id_counter += 1
    return new_student

@app.get("/students", response_model=List[StudentResponse])
def read_students():
    return students_db

@app.get("/students/{id}", response_model=StudentResponse)
def read_student_endpoint(id: int):
    for student in students_db:
        if student.id == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{id}", response_model=StudentResponse)
def update_student_endpoint(id: int, student_update: Student):
    for index, student in enumerate(students_db):
        if student.id == id:
            updated_student = StudentResponse(id=id, **student_update.dict())
            students_db[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{id}")
def delete_student_endpoint(id: int):
    for index, student in enumerate(students_db):
        if student.id == id:
            del students_db[index]
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")