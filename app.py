import os

from flask import Flask

from api.routes import bp
from api.student import students_bp
from database import migrate, db
from settings import settings

config_variable_name = 'FLASK_CONFIG_PATH'
default_config_path = os.path.join(os.path.dirname(__file__), 'config/local.py')
os.environ.setdefault(config_variable_name, default_config_path)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URL
    app.register_blueprint(bp)
    app.register_blueprint(students_bp)
    init_app(app)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200

    @app.route('/students', methods=['GET'])
    def get_students():
        db_session: Session = db.session
        name_filter = request.args.get('name')
        query = select(Student)
        if name_filter:
            query = query.where(Student.name.ilike(f"%{name_filter}%"))
        students = db_session.scalars(query).all()
        student_models = [StudentRead.from_orm(student).dict() for student in students]
        return jsonify(student_models)

    return app


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)