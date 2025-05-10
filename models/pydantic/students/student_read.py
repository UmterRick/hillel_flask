from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class StudentReadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    surname: str
    email: str
    group: str
    course_name: Optional[str] = None
    photo_url: Optional[str] = None
    birth_date: date