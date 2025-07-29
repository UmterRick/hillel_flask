from pydantic import BaseModel, Field
from datetime import date


class StudentCreateModel(BaseModel):
    name: str
    birth_date: date
    course: str
    photo_url: str