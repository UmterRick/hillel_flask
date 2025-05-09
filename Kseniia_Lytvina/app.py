from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Kseniia",
        "birthdate": "2003-05-30",
        "course_name": "PyPro",
        "photo_url": "http://127.0.0.1:5000/static/photo.JPG"
    },
    {
        "id": 2,
        "name": "Snickers",
        "birthdate": "2017-07-27",
        "course_name": "IT-Cats",
        "photo_url": "http://127.0.0.1:5000/static/cat.jpg"
    }
]

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

@app.route('/health')
def health_check():
    return {"status": "ok"}, 200

@app.route('/students')
def get_students():
    search_name = request.args.get("name")
    filtered_students = []

    for student in students:
        if not search_name or search_name.lower() in student["name"].lower():
            student_copy = student.copy()
            student_copy["age"] = calculate_age(student["birthdate"])
            filtered_students.append(student_copy)

    return jsonify(filtered_students)

if __name__ == "__main__":
    app.run(debug=True)