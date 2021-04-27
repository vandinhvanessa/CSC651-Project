from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Numeric, ARRAY
from sqlalchemy.orm import relationship

from app.sql_db.database import Base

"""
This file has the SQLAlchemy database models that are used to generate the database tables.
It will have much more in the future as we add users, etc.

"""


# =====Main Tables=====

class Employees(Base):
    __tablename__ = "Employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    position = Column(String(20))
    salary = Column(Integer)
    email = Column(String(50), unique=True)
    phone = Column(String(12))
