from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import database
from models.career import EducationLevel
from routes import career, contact
from schemas.career import JobApplicationSchema
from schemas.contact import ContactFormCreate

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router, prefix="/contact", tags=["Contact"])
app.include_router(career.router, prefix="/career", tags=["Career"])

database.Base.metadata.create_all(bind=database.engine)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def home():
    return {"message": "API is running"}

def insert_education_levels():
    db = next(database.get_db())
    levels = ["High School", "Bachelor's", "Master's", "PhD"]
    existing_levels = db.query(EducationLevel).count()
    if existing_levels == 0:  # ✅ Insert only if table is empty
        db.add_all([EducationLevel(name=level) for level in levels])
        db.commit()

@app.on_event("startup")
def startup_event():
    insert_education_levels()  # ✅ Automatically insert education levels
