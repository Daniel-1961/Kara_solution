from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

@app.post("/items/", response_model=schemas.MedicalItemResponse)
def create_item(item: schemas.MedicalItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_medical_item(db, item)

@app.get("/items/", response_model=list[schemas.MedicalItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_medical_items(db, skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.MedicalItemResponse)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.get_medical_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
