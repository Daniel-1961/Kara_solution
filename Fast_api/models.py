from sqlalchemy import Column, Integer, String
from .database import Base

class MedicalItem(Base):
    __tablename__ = "medical_items"  # Table name in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    name = Column(String, index=True)  # Medical item name
    category = Column(String)  # Category (e.g., surgical tools, medicine)
    price = Column(Integer)  # Price of the item
