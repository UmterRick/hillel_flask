# routes.py

from flask import Blueprint, jsonify, render_template
from .models import Student
from . import db
from flask import request
from datetime import datetime
from .schemas import StudentSchema


main = Blueprint("main", __name__)


@main.route("/students", methods=["GET"])
def get_students():

    students = Student.query.all()

    result = [StudentSchema.model_validate(student).model_dump() for student in students]
    return jsonify(result)


@main.route("/add_student", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data.get("name")
    birth_date = datetime.strptime(data.get("birth_date"), "%Y-%m-%d").date()
    course_name = data.get("course_name")
    photo_url = data.get("photo_url")

    new_student = Student(name=name, birth_date = birth_date, course_name = course_name, photo_url = photo_url)

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Студента додано"}), 201


@main.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_student(id):

    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Студента не знайдено"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Студента видалено"}), 200


@main.route("/update_student/<int:id>", methods=["PUT"])
def update_student(id):

    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Студента не знайдено"}), 404

    data = request.get_json()
    student.name = data.get("name", student.name)
    student.birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
    student.course_name = data.get("course_name", student.course_name)
    student.photo_url = data.get("photo_url", student.photo_url)

    db.session.commit()
    return jsonify({"message": "Студента оновлено"}), 200


@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok"}), 200


@main.route('/students_ui', methods=['GET'])
def students_ui():
    search_name = request.args.get("search_name")

    if search_name:
        students = Student.query.filter(Student.name.ilike(f"%{search_name}%")).all()
    else:
        students = Student.query.all()

    return render_template("students.html", students=students)