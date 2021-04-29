from app.sql_db import crud, schemas
from app.sql_db.database import get_db

from fastapi import APIRouter, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session

from typing import List, Optional

import os.path
import uuid

# instantiates an APIRouter
router = APIRouter()

# get employees 
@router.get("/", response_class=HTMLResponse)
async def get_add_employee_page():
    with open("/var/www/html/employeeAdd.html") as f:
        html = f.read()

    return html

@router.post("/", response_class=HTMLResponse)
async def get_add_employee_page(db: Session = Depends(get_db),
                                name: str = Form(...),
                                position: str = Form(...),
                                salary: int = Form(...),
                                email: str = Form(...),
                                phone: str = Form(...)):

    crud.create_employee(db, name, position, salary, email, phone)
