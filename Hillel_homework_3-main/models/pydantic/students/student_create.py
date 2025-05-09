from datetime import date

from pydantic import BaseModel


class StudentUpdateModel(BaseModel):
    name: str
    birth_date: date