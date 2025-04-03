
from sqlalchemy.orm import Session
import models.contact as models
import schemas.contact as schemas

class ContactService:
    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, contact: schemas.ContactFormCreate):
        db_contact = models.ContactForm(**contact.dict())
        self.db.add(db_contact)
        self.db.commit()
        self.db.refresh(db_contact)
        return db_contact

    def get_all_contacts(self):
        return self.db.query(models.ContactForm).all() 