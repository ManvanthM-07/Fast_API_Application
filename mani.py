from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    age: int
    Roll_number:str
    Department:str


@app.get("/")
def read_root():
    return {"Hello": "World"}

class StudentResponse(Student):
    id: int
   

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student(student:Student)->StudentResponse:
    students.append(student)
    return student

def get_student_by_roll(roll):
    for student in students:
        if student.Roll_number == roll:
            return student


def read_student(roll:int)->StudentResponse:
    return get_student_by_roll(roll)


def update_student(roll:int,student:Student)->StudentResponse:
    return StudentResponse(Roll_number=roll, **student.dict())

def delete_student(roll:int):
    return StudentResponse(Roll_number=roll, **student.dict())

@app.get("/students")
def read_students():
    return students

@app.post("/students")
def create_student_api(student:Student):
    return create_student(student)

@app.get("/students/{roll}")
def read_student_api(roll:int):
    return read_student(id)

@app.put("/students/{roll}")
def update_student_api(roll:int,student:Student):
    return update_student(id,student)

@app.delete("/students/{id}")
def delete_student_api(id:int):
    return delete_student(id)