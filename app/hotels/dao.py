from datetime import date
from app.dao.base import BaseDAO
from sqlalchemy import select

from app.database import engine, async_session_maker
from app.hotels.models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def add(
        cls,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
    ):
        pass