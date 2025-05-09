import click
import datetime
from flask.cli import with_appcontext
from database import db
from api.student import Student


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()

    # Create a sample student
    student = Student(
        name='John Doe',
        birth_date=datetime.datetime.strptime('2000-01-01', '%Y-%m-%d').date(),
        course_name='Computer Science',
        photo_url='https://example.com/photo.jpg'
    )
    db.session.add(student)

    try:
        db.session.commit()
        click.echo('Initialized the database with sample data.')
    except Exception as e:
        db.session.rollback()
        click.echo(f'Error: {str(e)}')


def init_app(app):
    app.cli.add_command(init_db_command)