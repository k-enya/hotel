from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from dataclasses import dataclass

app = FastAPI()

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

@dataclass
class HotelSearchArgs: #схема для аргументов
    location: str #обязательные параметры
    date_from: date
    date_to: date
    has_spa: bool = None #опциональный параметр
    stars: int = Query(None, ge=1, le=5) #опциональный параметр

@app.get('/hotels')
def get_hotels(
        search_args: HotelSearchArgs = Depends()
) -> list[SHotel]: #пост запрос
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