from datetime import date
from typing import Optional
from pydantic import BaseModel


class StudentCreateModel(BaseModel):
    name: str
    birth_date: date
    course: Optional[str] = None
    photo_url: Optional[str] = None