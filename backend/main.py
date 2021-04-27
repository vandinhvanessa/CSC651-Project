from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse 

from app.routers import employee

from app.sql_db import models

from app.sql_db.database import SessionLocal, engine

# build tables in the database
#models.Base.metadata.create_all(bind=engine)


# build tables in the database
models.Base.metadata.create_all(bind=engine)

# create an instance of the fastAPI app
app = FastAPI()


# redirect root of the site to our homepage

@app.get("/")
async def root():
    return RedirectResponse(url='/html/index.html')

app.include_router(employee.router)

app.include_router(
        employee.router,
        prefix="/employee",
        tags=["employee"]
)

# include the routers
#app.include_router(login)

# mount static files
app.mount("/", StaticFiles(directory=".."), name="static")
