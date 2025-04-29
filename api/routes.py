<<<<<<< HEAD
=======
from markupsafe import escape
>>>>>>> 5d80988 (flask project)
from flask import jsonify, Blueprint, render_template

from database import db
from  models.sqlalchemy.student import Student
bp = Blueprint("main_bp", __name__, url_prefix="/")

@bp.route('/')
def home() -> str:
<<<<<<< HEAD
    return render_template('home_page.html')

@bp.route("/test", methods=["DELETE"])
=======
    return render_template(escape('home_page.html'))

@bp.route("/test")
#@bp.route("/test", methods=["DELETE"])
>>>>>>> 5d80988 (flask project)
def route_test():
    db.session.get(Student, 1)
    return jsonify({"message": "Hello"}), 200

@bp.route("/new-test")
def route_test_2():
    return jsonify({"message": "Hello 2"}), 200

<<<<<<< HEAD



=======
###
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
>>>>>>> 5d80988 (flask project)
