from database import db
from datetime import date


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    course = db.Column(db.String(100), nullable=True)       #додавання назви курсу
    photo_url = db.Column(db.String(255), nullable=True)    #додавання фото

    def to_dict(self):
        return {
            "student_id": self.id,
            "name": self.name,
            "birth_date": self.birth_date.isoformat(),
            "course": self.course,
            "photo_url": self.photo_url,
            "age": self.get_age()
        }

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )