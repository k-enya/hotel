from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.database import Base

class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer, nullable=False)
    image_is = Column(Integer)

    hotel = relationship("Hotels", back_populates="rooms")
    booking = relationship("Bookings", back_populates="rooms")


