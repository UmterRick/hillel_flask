from database import db


class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    ###
    # last_name = db.Column(db.String(100), nullable=True)
    course_name = db.Column(db.String(200), nullable=True)
    photo_url = db.Column(db.String(500), nullable=True)
    # email= db.Column(db.String(100), nullable=False)

