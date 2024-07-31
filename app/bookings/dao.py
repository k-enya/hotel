from datetime import date, timedelta

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from sqlalchemy import select, and_, func, insert

from app.database import engine, async_session_maker
from app.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        """
        with request_dates as (
        select generate_series(
        arrive::date_from,
        departure::date_to,
        '1 day'
        )::date day_,
        user_id,
        room_id::numeric
        from request
        )

        select
        day_, request_dates.room_id,
        rooms.quantity total_rooms,
        count(bookings.id) booked_rooms,
        rooms.quantity - count(bookings.id) free_rooms
        from request_dates
        left join rooms on rooms.id = request_dates.room_id
        left join bookings on bookings.room_id = request_dates.room_id
        and request_dates.day_ between bookings.date_from and bookings.date_to
        group by day_, request_dates.room_id, rooms.quantity
        order by 1
        """
        async with async_session_maker() as session:
            request_dates = select(func.generate_series(date_from, date_to, timedelta(days=1)).label("day_"),
                                   room_id).subquery()

            print(request_dates)

            get_rooms_left = select(
                request_dates.c.day_,
                request_dates.c.room_id,
                Rooms.quantity,
                func.count(Bookings.id).label('booked_rooms'),
                (Rooms.quantity - func.count(Bookings.id)).label('free_rooms').select_from(request_dates)
            ).join(
                Rooms, Rooms.id == request_dates.c.room_id, isouter=True).outerjoin(
                Bookings,
                and_(Bookings.room_id == request_dates.c.room_id,
                     request_dates.c.day_.between(Bookings.date_from, Bookings.date_to)
                     )
            ).group_by(request_dates.c.day_, request_dates.c.room_id, Rooms.quantity
                       ).order_by(Rooms.quantity - func.count(Bookings.id).asc()).all()

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()

            else:
                return None
