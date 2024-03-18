from datetimerange import DateTimeRange
from .booking_price_calculator import BookingPriceCalculator
from enum import Enum

class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3

class Booking:
    def __init__(self, room, start, end):
        self.room = room
        self.start = start
        self.end = end
        self.period = DateTimeRange(self.start, self.end)
        self.id = None
        self.status = BookingStatus.PENDING

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, BookingStatus):
            raise ValueError("status must be a BookingStatus")
        self._status = value

    def price(self):
        return BookingPriceCalculator(self.room.price_day, self.period).calculate()

    def __str__(self):
        return f"room: {self.room} - start: {self.start} end: {self.end}"

    def __repr__(self):
        return f"booking<id: {self.id} room: {self.room} start: {self.start} end: {self.end}>"
