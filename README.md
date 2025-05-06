# Install poetry
pip install poetry

install flask
install flask-sqlalchemy (Database ORM)
install flask-migrate (Alembic for Database version system, migration)


1) Create Flask App
2) Config App (specify db url and others settings...)
3) Init DB and link Migration to db
Start own development
4) Define database tables with sqlalchemy models
5) Organize API routes using Flask Blueprints
6) Create API business logic (create routes functions)
7) Test your API with browser or/and Postman
8) (Optional) Create frontend part




=======
# PythonProject4
A simple Flask app for managing student data.

## Installation

1. Install Poetry (dependency management tool):
```bash
pip install poetry
```


install flask install flask-sqlalchemy (Database ORM) install flask-migrate (Alembic for Database version system, migration)

Create Flask App
Config App (specify db url and others settings...)
Init DB and link Migration to db Start own development
Define database tables with sqlalchemy models
Organize API routes using Flask Blueprints
Create API business logic (create routes functions)
Test your API with browser or/and Postman
(Optional) Create frontend part


After updating the migration file:
-First, remove any existing migration files that might have been created:

rm -f migrations/versions/*.py

-Then create a new migration:

flask db migrate -m "add course_name and photo_url to student"

-Apply the migration:

flask db upgrade



