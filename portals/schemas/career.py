from pydantic import BaseModel, EmailStr, HttpUrl, validator
import re


class EducationLevelSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model


class JobApplicationSchema(BaseModel):
    first_name: str
    last_name: str
    email_address: EmailStr
    phone_number: str
    address_line1: str
    city: str
    zip_code: str
    education_level_id: int
    institute_name: str
    resume_url: HttpUrl  
    why_to_join: str

    @validator("zip_code")
    def validate_zip_code(cls, value):
        if not re.match(r"^\d{5,6}$", value): 
            raise ValueError("Zip code must be 5-6 digits.")
        return value

    @validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r"^\d{10,15}$", value):  
            raise ValueError("Phone number must be between 10-15 digits.")
        return value

    @validator("why_to_join")
    def validate_why_to_join(cls, value):
        word_count = len(value.split())
        if word_count > 100: 
            raise ValueError("The 'Why to Join' section must not exceed 100 words.")
        return value

    class Config:
        from_attributes = True  # Allows ORM mode (SQLAlchemy integration)
