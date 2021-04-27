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
@router.get("/getEmployees/", response_model=List[schemas.Employee])
async def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

# post listing
'''
@router.post("/", response_model=schemas.Listing)
async def create_listing(db: Session = Depends(get_db),
                         user: schemas.User = Depends(get_current_user),
                         name: str = Form(...),
                         price: int = Form(...),
                         category: str = Form(...),
                         course: Optional[str] = Form(None),
                         description: str = Form(...),
                         images: List[UploadFile] = File(...)):
    # create new listing object
    listing = schemas.Listing(name=name, description=description, price=price, seller_id=user.id, course=course)
    photoPaths = []

    for file in images:
        # create random file names for image and thumbnail
        imgName = str(uuid.uuid4())
        thmbName = str(uuid.uuid4())

        fileType = '.png'

        # construct file paths
        imgPath = "/images/" + imgName + fileType
        thmbPath = "/images/" + thmbName + fileType

        photoPaths.append((imgPath, thmbPath))

        # save as full-sized image
        img = Image.open(file.file)
        img.save('/var/www' + imgPath, img.format)

        # save as thumbnail
        img = resizeimage.resize_contain(img, [256, 256], bg_color=(0, 0, 0, 0))
        img.save('/var/www' + thmbPath, img.format)
        img.close()

    return crud.create_listing(db, listing, photoPaths, category)
'''
