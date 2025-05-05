#Routes

from flask import Blueprint, jsonify, render_template, request

from database import db
from  models.sqlalchemy.student import Student

bp = Blueprint("main_bp", __name__, url_prefix="/")

@bp.route('/')
def home() -> str:
    return render_template('home_page.html')




@bp.route("/test", methods=["DELETE"])
def route_test():
    db.session.get(Student, 1)
    return jsonify({"message": "Hello"}), 200

@bp.route("/new-test")
def route_test_2():
    return jsonify({"message": "Hello 2"}), 200

#реалізація ендпоінту (точки перевірки стану): /health
@bp.route("/health", methods=["GET"])
def health_check():
    return {"message": "ok"}, 200

#Добавляємо ендпоінт /student для обробки параметра name:
@bp.route("/students", methods=["GET"])
def get_students():
    name_filter = request.args.get("name", "").strip()
    query = db.session.query(Student)
    if name_filter:
        query = query.filter(Student.name.ilike(f"%{name_filter}%"))
    students = query.all()
    return jsonify({"students": [s.to_dict() for s in students]})