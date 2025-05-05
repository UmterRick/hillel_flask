from datetime import date
from typing import Optional
from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[date] = None
    course: Optional[str] = None
    photo_url: Optional[str] = None



