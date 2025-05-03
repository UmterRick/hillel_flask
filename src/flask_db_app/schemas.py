from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class StudentSchema(BaseModel):
    id: int
    name: str
    birth_date: date
    course_name: str
    photo_url: str
    age: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

    def model_post_init(self, __context):
        today = date.today()
        self.age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )