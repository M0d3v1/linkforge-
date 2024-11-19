from app.celery.celery_app import celery_app
from app.models.analytics import Analytics
from sqlalchemy.orm import Session
from app.db import SessionLocal

@celery_app.task
def log_analytics(short_code: str, user_agent: str, ip_address: str):
    db: Session = SessionLocal()
    new_entry = Analytics(
        short_code=short_code,
        user_agent=user_agent,
        ip_address=ip_address,
    )
    db.add(new_entry)
    db.commit()
