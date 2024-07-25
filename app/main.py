from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from dataclasses import dataclass
from app.dao.base import BaseDAO

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)

