
from sqlalchemy import Column, Integer, String
from database import Base

class ContactForm(Base):
    __tablename__ = "contact_form"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email_address = Column(String, unique=True, index=True)
    interest = Column(String) 
    message = Column(String)
    find_us = Column(String)
