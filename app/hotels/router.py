from datetime import date

from fastapi import APIRouter
from sqlalchemy import select, and_, func, insert

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.exceptions import RoomCannotBeBooked
from app.hotels.dao import HotelsDAO
from app.hotels.rooms.models import Rooms
from app.hotels.schemas import SHotels

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

@router.get("")
async def get_hotels(
        location: str, date_from: date, date_to: date
) -> list[SHotels]:
        pass
