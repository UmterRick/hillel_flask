from datetime import date
from pydantic import BaseModel, ConfigDict, Field, computed_field


class StudentReadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int = Field(alias="id")
    name: str
    birth_date: date
    ###
    # last_name: str
    course_name: str
    photo_url: str | None = None

    @computed_field
    def age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
                today.month == self.birth_date.month and
                today.day < self.birth_date.day
        ):
            age -= 1
        return age
