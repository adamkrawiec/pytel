from datetime import datetime, timedelta
from datetimerange import DateTimeRange
from hotel.booking import Booking, BookingRepository

class Room:
    id = 0
    rooms = []

    @classmethod
    def all(cls):
      return cls.rooms

    def __init__(self, hotel, price_day):
        self.hotel = hotel
        self.price_day = price_day
        Room.id += 1
        self.id = Room.id
        Room.rooms.append(self)
    
    def bookings(self):
        return [booking for booking in BookingRepository().all() if booking.room == self]
  
    def book(self, start, end):
        if self.is_booked_between(start, end):
            raise ValueError("Room is already booked for this date range")
        return Booking(self, start, end).save()
  
    def is_booked_between(self, start, end):
        date_range = DateTimeRange(start, end).range(timedelta(days=1))
        return any(
          self.is_booked_on(date) for date in date_range
        )
    
    def is_booked_on(self, date):
        return any(
          date in booking.period for booking in self.bookings()
        )

    def __str__(self):
        return f"hotel: {self.hotel} id: {self.id}"

    def __repr__(self):
        return f"room<hotel: {self.hotel} id: {self.id}>"
