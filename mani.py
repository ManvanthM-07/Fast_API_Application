from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()
class student(BaseModel):
    Name: str
    Email: str
    age: int
    Roll_no: int
    Department: str
    
    class student_response(BaseModel):
        name: str
        email: str
        age: int
        Roll_no: int
        Department: str

@app.get("/")
def read_root():
    return {"Hello": "World"} 
    
def create_student(student: student) 
    return studentresponse(id=id, **student.dict())
 def read_student(id: int):
        return student
def update_student(id: int, student: student):
    return studentresponse(id=id, **student.dict())
def delete_student(id: int):
    return studentresponse(id=id, **student.dict())

@app.post("/students")
def create_student(student: student):
    return create_student(student)

@app.get("/students")
def read_student(id: int):
    return read_student(id)

@app.put("/students/{id}")
def update_student(id: int, student: student):
    return update_student(id, student)

@app.delete("/students/{id}")
def delete_student(id: int):
    return delete_student(id)