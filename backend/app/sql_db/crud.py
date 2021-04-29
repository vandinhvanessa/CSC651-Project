import datetime

from typing import List

from sqlalchemy import desc, asc, or_
from sqlalchemy.orm import Session

from app.sql_db import models, schemas

"""
This file is used for the 4 big interactions with the database: create, read, update, & delete.

Author(s): This file contains logic for many routers, all team members contributed
"""


def get_employees(db: Session):
    return db.query(models.Employees).all()

def create_employee(db: Session, name, position, salary, email, phone):
    employee = models.Employees()
    employee.name = name
    employee.position = position
    employee.salary = salary
    employee.email = email
    employee.phone = phone
    
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee 


