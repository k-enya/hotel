from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/booking",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()