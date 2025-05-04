from datetime import datetime
from database import db


class Student(db.Model):
    __tablename__ = "students"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    course_name = db.Column(db.String, nullable=True)  # Назва курсу
    photo_url = db.Column(db.String, nullable=True)  # URL до фотографії
    current_health = db.Column(db.Integer, default=100)  # Поточне здоров'я студента

    @property
    def age(self):
        """Вираховує вік студента на основі дати народження."""
        today = datetime.today()
        return (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )

    @property
    def max_health(self):
        """Максимальне здоров'я залежить від віку студента"""
        if self.age <= 20:
            return 100  # Вік 0-20 років — максимальне здоров'я 100
        elif 21 <= self.age <= 40:
            return 80  # Вік 21-40 років — максимальне здоров'я 80
        else:
            return 60  # Вік 41+ років — максимальне здоров'я 60

    @property
    def health(self):
        """Поточне здоров'я студента"""
        return self.current_health

    def damage(self, amount: int):
        """Метод для зменшення здоров'я студента"""
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0  # Здоров'я не може бути менше 0
        db.session.commit()  # Зберігаємо зміни в базі даних
