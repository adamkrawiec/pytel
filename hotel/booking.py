from datetimerange import DateTimeRange
from .booking_price_calculator import BookingPriceCalculator
from .booking_repository import BookingRepository

class Booking:
    def __init__(self, room, start, end):
        self.room = room
        self.start = start
        self.end = end
        self.period = DateTimeRange(self.start, self.end)
        self.id = None

    def save(self):
        self.id = BookingRepository().persist(self).id
        return self

    def price(self):
        return BookingPriceCalculator(self.room.price_day, self.period).calculate()

    def __str__(self):
        return f"room: {self.room} - start: {self.start} end: {self.end}"

    def __repr__(self):
        return f"booking<id: {self.id} room: {self.room} start: {self.start} end: {self.end}>"
