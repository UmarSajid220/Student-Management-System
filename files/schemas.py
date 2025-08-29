from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    course: str
    grade: str
    id: int

class Student(StudentCreate):
    id: int
