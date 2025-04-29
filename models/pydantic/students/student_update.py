from datetime import date

from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name:str | None = None
<<<<<<< HEAD
    birth_date: date | None = None
=======
    birth_date: date | None = None
    ###
    #last_name: str | None = None
    course_name: str
    photo_url: str| None=None
>>>>>>> 5d80988 (flask project)
