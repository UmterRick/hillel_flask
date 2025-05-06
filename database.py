from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

# def init_db(flask_app):
#     sql_db.init_app(flask_app)
#     migrate.init_app(flask_app, sql_db)
#     return sql_db
