from datetime import date

from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name: str
    birth_date: date
    ###
    # last_name:
    course_name: str
    photo_url: str | None = None
