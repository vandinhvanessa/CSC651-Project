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

def create_employee(db: Session, employee: schemas.Employee):
    db_user = models.Employees(name = employee.name, position = employee.position, start = employee.start, salary = employee.salary,
            email = employee.email, phone = employee.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


