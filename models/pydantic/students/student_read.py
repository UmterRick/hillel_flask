from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class StudentReadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int = Field(alias="id")
    name: str
    birth_date: date
    course_name: str | None = Field(default=None)
    photo_url: str | None = Field(default=None)
    current_health: int | None = Field(default=None)
    age: int | None = Field(default=None)
