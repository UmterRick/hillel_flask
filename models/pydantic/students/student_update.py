from pydantic import BaseModel
from typing import Optional
from datetime import date


class StudentUpdateModel(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[date] = None
    course: Optional[str] = None
    photo_url: Optional[str] = None
