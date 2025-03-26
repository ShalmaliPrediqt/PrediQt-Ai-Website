from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
from routes import contact
from schemas.contact import ContactFormCreate



app = FastAPI()

# Apply CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Contact API Routes
app.include_router(contact.router)

# Ensure tables are created (ONLY for SQLite, not PostgreSQL)
database.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def home():
    return {"message": "API is running"}
