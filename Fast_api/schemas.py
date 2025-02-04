from pydantic import BaseModel

class MedicalItemBase(BaseModel):
    name: str
    category: str
    price: int

class MedicalItemCreate(MedicalItemBase):
    pass

class MedicalItemResponse(MedicalItemBase):
    id: int

    class Config:
        from_attributes = True
