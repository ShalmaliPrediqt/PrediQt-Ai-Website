from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from database import get_db
from schemas.career import EducationLevelSchema, JobApplicationSchema
from services.career_service import JobApplicationService , EducationService

router = APIRouter()

@router.post("/apply", response_model=JobApplicationSchema)
async def apply_for_job(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email_address: str = Form(...),
    phone_number: str = Form(...),
    address_line1: str = Form(...),
    city: str = Form(...),
    zip_code: str = Form(...),
    education_level_id: int = Form(...),
    institute_name: str = Form(...),
    why_to_join: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    service = JobApplicationService(db) 

    
    resume_url = service.save_resume(resume, email_address)

    job_application = service.create_job_application(
        JobApplicationSchema(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            address_line1=address_line1,
            city=city,
            zip_code=zip_code,
            education_level_id=education_level_id,
            institute_name=institute_name,
            resume_url=resume_url, 
            why_to_join=why_to_join
        ), 
        resume_url
    )

    return job_application

@router.get("/applications", response_model=list[JobApplicationSchema])
def get_applications(db: Session = Depends(get_db)):
    """Fetch all job applications"""
    service = JobApplicationService(db)
    return service.get_all_applications()

@router.get("/education-levels", response_model=list[EducationLevelSchema])
def get_education_levels(db: Session = Depends(get_db)):
    """Fetch all education levels"""
    service = EducationService(db)
    return service.get_all_education_levels()
