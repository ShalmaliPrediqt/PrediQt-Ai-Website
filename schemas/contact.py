from typing import ClassVar
from pydantic import BaseModel, EmailStr, validator
from enum import Enum

# Enum to restrict the values of interest
class InterestEnum(str, Enum):
    client = "Client"
    partner = "Partner"
    vendor = "Vendor"

class ContactFormCreate(BaseModel):
    full_name: str
    email_address: EmailStr  
    interest: InterestEnum  # Use the Enum for interest
    message: str
    find_us: str
    

    MAX_MESSAGE_WORDS: ClassVar[int] = 500
    MAX_FIND_US_WORDS: ClassVar[int] = 50

  
    @validator('message')
    def check_message_word_limit(cls, v):
        word_count = len(v.split())
        if word_count > cls.MAX_MESSAGE_WORDS:
            raise ValueError(f"Message should not exceed {cls.MAX_MESSAGE_WORDS} words. Currently {word_count} words.")
        return v

    @validator('find_us')
    def check_find_us_word_limit(cls, v):
        word_count = len(v.split())
        if word_count > cls.MAX_FIND_US_WORDS:
            raise ValueError(f"'Find Us' should not exceed {cls.MAX_FIND_US_WORDS} words. Currently {word_count} words.")
        return v
    
    class Config:
        from_attributes = True
