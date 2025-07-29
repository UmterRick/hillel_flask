from pydantic import BaseModel, computed_field
from datetime import date
from typing import Optional

class StudentReadModel(BaseModel):
    id: int
    name: str
    birth_date: date
    course: Optional[str]
    photo_url: Optional[str]

    @computed_field(return_type=int)
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    class Config:
        from_attributes = True
