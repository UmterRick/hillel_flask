from datetime import date
from typing import Optional
from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None
    group: Optional[str] = None
    course_name: Optional[str] = None
    photo_url: Optional[str] = None
    birth_date: Optional[date] = None
