# Student Management System (Beginner Project)

This is a beginner-friendly **Student Management System** built with **FastAPI**.  
It stores student data in a JSON file instead of a database, making it simple to set up and easy to understand for beginners.

---

## Features
- Add a new student with name, age, email, course, and grade.
- View details of a specific student by ID.
- Update student information.
- Delete a student.
- Stores all data in a `data.json` file.

---

## Project Structure
```
project/
├── files/
│   ├── data/
│   │   └── data.json        # JSON file where student data is saved
│   ├── schemas.py           # Pydantic models for validation
├── utils.py                 # Helper functions for reading and writing JSON
├── crud.py                  # Core API routes and CRUD logic
├── main.py                  # Entry point to run the app
└── README.md                # This file
```

---

## Requirements
- Python 3.8 or above
- FastAPI
- Uvicorn

---

## Installation
1. **Clone this repository** or copy the files into a folder.
2. Open a terminal in the project folder.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

---

## Running the Server
Run:
```bash
python main.py
```

Then visit:
- Interactive API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI Schema: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## Example Usage

### **1. Add a Student (POST)**
**Endpoint:** `POST /students/`

Example JSON body:
```json
{
  "name": "John Doe",
  "age": 20,
  "email": "johndoe@example.com",
  "course": "Python Basics",
  "grade": "A"
}
```
Example response:
```json
{
  "name": "John Doe",
  "age": 20,
  "email": "johndoe@example.com",
  "course": "Python Basics",
  "grade": "A",
  "id": 1
}
```

---

### **2. Get a Student (GET)**
**Endpoint:** `GET /students/{id}`  
Example:  
`GET /students/1`

Example response:
```json
{
  "name": "John Doe",
  "age": 20,
  "email": "johndoe@example.com",
  "course": "Python Basics",
  "grade": "A",
  "id": 1
}
```

---

### **3. Update a Student (PUT)**
**Endpoint:** `PUT /students/{id}`  
Example JSON body:
```json
{
  "name": "John Doe",
  "age": 21,
  "email": "johndoe@example.com",
  "course": "Advanced Python",
  "grade": "A+"
}
```
Example response:
```json
{
  "message": "Student updated successfully",
  "item": {
    "name": "John Doe",
    "age": 21,
    "email": "johndoe@example.com",
    "course": "Advanced Python",
    "grade": "A+",
    "id": 1
  }
}
```

---

### **4. Delete a Student (DELETE)**
**Endpoint:** `DELETE /students/{id}`  
Example:  
`DELETE /students/1`

Example response:
```json
{
  "message": "Student deleted successfully",
  "item": {
    "name": "John Doe",
    "age": 21,
    "email": "johndoe@example.com",
    "course": "Advanced Python",
    "grade": "A+",
    "id": 1
  }
}
```

---

## Notes
- The project uses **JSON for data storage**, so it is **not production-ready**.
- If `data.json` does not exist, it will be created automatically.
- To reset data, just delete `data.json` and restart the server.

---

## License
This project is open-source and free to use for learning purposes.
