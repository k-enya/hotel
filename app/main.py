from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool = Query(None),
        stars: int = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get('/hotels')
def get_hotels(
        search_args: HotelSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            'address': 'Подольск, ул. Х',
            'name': 'Super Hotel',
            'stars': '5'
        }
    ]
    return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post('/bokings')
def add_booking(booking: SBooking):
    pass