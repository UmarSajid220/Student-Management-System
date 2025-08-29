from fastapi import FastAPI, HTTPException
from files.schemas import Student, StudentCreate
from files.utils import read_json_file, write_json_file

app = FastAPI()


MAIN_DATA = "files/data/data.json"

@app.get("/")
async def root():
    return {"message": "Welcome to the Student Management System"}


@app.get("/students/{student_id}")
def get_student_data(student_id: int):
    students = read_json_file(MAIN_DATA)
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students/")
def post_student_data(student: StudentCreate):
    students = read_json_file(MAIN_DATA)
    if any(existing_student["id"] == student.id for existing_student in read_json_file(MAIN_DATA)):
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    new_student = student.dict()
    students.append(new_student)
    write_json_file(MAIN_DATA, students)
    return new_student

# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    students = read_json_file(MAIN_DATA)
    for i, student in enumerate(students):
        if student["id"] == student_id:
            students[i] = updated_student.dict()
            write_json_file(MAIN_DATA, students)
            return {"message": "Item updated successfully", "item": updated_student}
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students = read_json_file(MAIN_DATA)
    for i, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(i)
            write_json_file(MAIN_DATA, students)
            return {"message": "Item deleted successfully", "item": deleted_student}
    raise HTTPException(status_code=404, detail="Student not found")
