from datetime import date
from typing import Optional
from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    group: str
    course_name: Optional[str] = None
    photo_url: Optional[str] = None
    birth_date: date

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

