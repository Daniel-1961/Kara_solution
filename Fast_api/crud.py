from sqlalchemy.orm import Session
from . import models, schemas

def create_medical_item(db: Session, item: schemas.MedicalItemCreate):
    db_item = models.MedicalItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_medical_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MedicalItem).offset(skip).limit(limit).all()

def get_medical_item(db: Session, item_id: int):
    return db.query(models.MedicalItem).filter(models.MedicalItem.id == item_id).first()
