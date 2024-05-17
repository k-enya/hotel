from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashes_password = Column(String, nullable=False)

    booking = relationship("Bookings", back_populates="users")