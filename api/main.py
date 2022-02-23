from fastapi import FastAPI
from api.routers import geo


app = FastAPI()
app.include_router(geo.router)
