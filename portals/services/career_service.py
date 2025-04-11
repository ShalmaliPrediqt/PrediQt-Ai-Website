from sqlalchemy.orm import Session
from models.career import JobApplication
from schemas.career import JobApplicationSchema
from pathlib import Path
from urllib.parse import quote
from models.career import EducationLevel


UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

class JobApplicationService:
    def __init__(self, db: Session):
        self.db = db

    def generate_resume_url(self, filename: str) -> str:
        """Generate a direct URL for the uploaded resume"""
        base_url = "http://localhost:8000/uploads/"
        return f"{base_url}{quote(filename)}"

    def save_resume(self, resume, email_address: str) -> str:
        """Save the uploaded resume file locally and return the URL"""
        allowed_types = {
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
        if resume.content_type not in allowed_types:
            raise ValueError("Invalid file type. Only PDF, DOC, and DOCX are allowed.")

      
        file_extension = Path(resume.filename).suffix
        new_filename = f"{email_address}{file_extension}"
        file_location = UPLOAD_FOLDER / new_filename

        # Save the file locally
        with open(file_location, "wb") as buffer:
            buffer.write(resume.file.read())

        return self.generate_resume_url(new_filename)

    def create_job_application(self, application_data: JobApplicationSchema, resume_url: str):
       application_data_dict = application_data.dict()
    

        application_data_dict['resume_url'] = resume_url
    
    
        job_application = JobApplication(**application_data_dict)
        self.db.add(job_application)
        self.db.commit()
        self.db.refresh(job_application)
        return job_application


    def get_all_applications(self):
        return self.db.query(JobApplication).all()


class EducationService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_education_levels(self):
        return self.db.query(EducationLevel).all()
