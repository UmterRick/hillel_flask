# models.py

from . import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), nullable=False)

    birth_date = db.Column(db.Date, nullable=False)

    course_name = db.Column(db.String(120), nullable=False)

    photo_url = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return f"<Student {self.name}>"