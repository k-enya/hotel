from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from dataclasses import dataclass
from app.dao.base import BaseDAO

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


