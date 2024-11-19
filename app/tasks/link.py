from app.celery.celery_app import celery_app
from app.models.link import Link
from sqlalchemy.orm import Session
from app.db import SessionLocal

@celery_app.task
def increment_clicks(short_code: str):
    db: Session = SessionLocal()
    link = db.query(Link).filter(Link.short_code == short_code).first()
    if link:
        link.clicks += 1
        db.commit()
