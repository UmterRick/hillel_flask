from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date
from database import db
import datetime


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    birth_date: Mapped[Date] = mapped_column(Date, nullable=False)
    course_name: Mapped[str] = mapped_column(String, nullable=True)
    photo_url: Mapped[str] = mapped_column(String, nullable=True)

    def age(self):
        today = datetime.date.today()
        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', surname='{self.surname}')>"
