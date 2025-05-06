from flask import Blueprint, request, jsonify
from database import db
from models.pydantic.students.student_read import StudentReadModel
from models.pydantic.students.student_update import StudentUpdateModel
from models.sqlalchemy.student import Student
from sqlalchemy import or_


students_bp = Blueprint("students_bp", __name__, url_prefix="/students")

# Fix 1: Add the GET route for individual student
@students_bp.route("/<int:pk>", methods=["GET"])
def get_student_by_id(pk):
    student = Student.query.get(pk)
    if student is None:
        return jsonify({"error": f"Student with id={pk} not found"}), 404
    return jsonify(StudentReadModel.model_validate(student).model_dump(mode="json"))

# Your existing routes
@students_bp.route("/<int:pk>", methods=["DELETE"])
def delete_student_by_id(pk):
    student = Student.query.get(pk)
    if student is None:
        return jsonify({"error": f"Student with id={pk} not found"}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student was successfully deleted"}), 204

@students_bp.route("/<int:pk>", methods=["PATCH"])
def edit_student_by_id(pk):
    student = Student.query.get(pk)
    if student is None:
        return jsonify({"error": f"Student with id={pk} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": f"No data provided"}), 400

    validated_data = StudentUpdateModel.model_validate(data)
    for field, value in validated_data.model_dump(exclude_none=True).items():
        if value is not None:
            setattr(student, field, value)
    db.session.commit()

    return jsonify(StudentReadModel.model_validate(student).model_dump(mode="json"))

@students_bp.route("/", methods=["POST"])
def create_student_by_id():  # Changed name to be more descriptive
    data = request.get_json()
    if not data:
        return jsonify({"error": f"No data provided"}), 400

    validated_data = StudentUpdateModel.model_validate(data)
    new_student = Student(**validated_data.model_dump())

    db.session.add(new_student)
    db.session.commit()

    return jsonify(StudentReadModel.model_validate(new_student).model_dump(mode="json")), 201

@students_bp.route("/", methods=['GET'])
def search_student():
    name_filter = request.args.get('name', '').strip()
    if name_filter:
        students = Student.query.filter(or_(Student.name.ilike(f'%{name_filter}%'))).all()
    else:
        students = Student.query.all()

    return jsonify({
        'students': [StudentReadModel.model_validate(student).model_dump() for student in students]
    })
