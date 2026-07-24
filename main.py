from fastapi import FastAPI
from database import Base, engine
from routers import room_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(room_router.router)
