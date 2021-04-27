import decimal
from typing import List
from datetime import datetime

from pydantic import BaseModel

"""
This file has the Pydantic models that are used to mirror the database tables as python objects.
This allows fastAPI to do some cool things like send http responses of json objects that match these classes.
"""


# =====Employee=====
class Employee(BaseModel):
    id: int
    name: str
    position: str
    salary: int
    email: str
    phone: str

    class Config:
        orm_mode = True

class Employees(BaseModel):
    employees: List[Employee]
