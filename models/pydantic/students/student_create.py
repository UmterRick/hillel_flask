from datetime import date

from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name: str
<<<<<<< HEAD
    birth_date: date
=======
    birth_date: date
    ###
    #last_name:
    course_name: str
    photo_url: str| None=None
>>>>>>> 5d80988 (flask project)
