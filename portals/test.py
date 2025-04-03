from sqlalchemy import text
from database import SessionLocal

db = SessionLocal()
result = db.execute(text("SELECT version();")).fetchone()
print(result)
