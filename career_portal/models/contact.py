from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class EducationLevel(Base):
    __tablename__ = "education_levels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    address_line1 = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(String(6), nullable=False)
    education_level_id = Column(Integer, ForeignKey("education_levels.id"), nullable=False)
    institute_name = Column(String, nullable=False)
    resume_url = Column(String, nullable=False)  # Store direct link
    why_to_join = Column(Text, nullable=False)

    education_level = relationship("EducationLevel")

    def __init__(self, first_name, last_name, email_address, phone_number, address_line1, city, zip_code, education_level_id, institute_name, resume_url, why_to_join):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.address_line1 = address_line1
        self.city = city
        self.zip_code = zip_code
        self.education_level_id = education_level_id
        self.institute_name = institute_name
        self.resume_url = resume_url
        self.why_to_join = why_to_join
