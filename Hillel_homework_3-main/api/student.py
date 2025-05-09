import datetime
from flask import Blueprint, jsonify, request
from database import db
from sqlalchemy.ext.hybrid import hybrid_property
import datetime
from dataclasses import dataclass

students_bp = Blueprint('students', __name__, url_prefix='/students')


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    course_name = db.Column(db.String(100), nullable=True)
    photo_url = db.Column(db.String(255), nullable=True)

    @hybrid_property
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


@dataclass
class StudentSchema:
    id: int
    name: str
    birth_date: str
    course_name: str
    photo_url: str
    age: int

    @classmethod
    def from_model(cls, student):
        return cls(
            id=student.id,
            name=student.name,
            birth_date=student.birth_date.strftime('%Y-%m-%d'),
            course_name=student.course_name,
            photo_url=student.photo_url,
            age=student.age
        )


@students_bp.route('/', methods=['GET'])
def get_students():
    name_filter = request.args.get('name', '')

    query = Student.query
    if name_filter:
        query = query.filter(Student.name.ilike(f'%{name_filter}%'))

    students = query.all()

    result = []
    for student in students:
        student_data = StudentSchema.from_model(student).__dict__
        result.append(student_data)

    return jsonify(result)


@students_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    student_data = StudentSchema.from_model(student).__dict__
    return jsonify(student_data)


@students_bp.route('/', methods=['POST'])
def create_student():
    data = request.json
    student = Student(
        name=data['name'],
        birth_date=datetime.datetime.strptime(data['birth_date'], '%Y-%m-%d').date(),
        course_name=data.get('course_name'),
        photo_url=data.get('photo_url')
    )
    db.session.add(student)
    db.session.commit()

    student_data = StudentSchema.from_model(student).__dict__
    return jsonify(student_data), 201


@students_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.json

    student.name = data['name']
    student.birth_date = datetime.datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
    student.course_name = data.get('course_name')
    student.photo_url = data.get('photo_url')

    db.session.commit()

    student_data = StudentSchema.from_model(student).__dict__
    return jsonify(student_data)


@students_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()

    return '', 204