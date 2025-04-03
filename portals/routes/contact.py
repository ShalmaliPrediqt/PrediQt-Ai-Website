from fastapi import APIRouter, Depends, HTTPException
#from grpc import services
from sqlalchemy.orm import Session
import models, schemas, database
import schemas.contact as schemas  # ✅ Import with Namespace
import services.contact_service as services



router = APIRouter()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit-contact", response_model=schemas.ContactFormCreate)
def submit_contact_form(contact: schemas.ContactFormCreate, db: Session = Depends(get_db)):
    return services.ContactService(db).create_contact(contact)

@router.get("/contacts", response_model=list[schemas.ContactFormCreate])
def get_contacts(db: Session = Depends(get_db)):
    contact_service = services.ContactService(db)
    return contact_service.get_all_contacts()