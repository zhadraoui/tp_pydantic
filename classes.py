from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, validator


class Medication(BaseModel):
    name: str
    dosage_mg: float
    start_date: date
    end_date: Optional[date] = None


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., pattern=r"^\d{5}$", description="Code postal à 5 chiffres")


class Patient(BaseModel):
    id: int
    full_name: str = Field(..., min_length=3)
    birth_date: date
    email: EmailStr
    address: Address
    medications: List[Medication] = []
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    @validator('birth_date')
    def validate_birth_date(cls, value):
        if value > date.today():
            raise ValueError("La date de naissance ne peut pas être dans le futur.")
        return value

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
