from .booking import Booking
from .booking_repository import BookingRepository

class BookingCreator:
    def __init__(self, room, start, end):
        self.room = room
        self.start = start
        self.end = end

    def create(self):
        if self.room.is_booked_between(self.start, self.end):
            raise ValueError("Room is already booked for this date range")
        booking = Booking(self.room, self.start, self.end)
        return BookingRepository().persist(booking)