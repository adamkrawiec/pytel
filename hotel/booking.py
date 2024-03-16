from datetimerange import DateTimeRange
from datetime import datetime, timedelta

class Booking:
    id = 0
    bookings = []

    def __init__(self, room, start, end):
        self.room = room
        self.start = start
        self.end = end
        self.period = DateTimeRange(self.start, self.end)
        Booking.id += 1
        self.id = Booking.id
        Booking.bookings.append(self)

    def price(self):
      date_range = [date for date in self.period.range(timedelta(days=1))]
      return self.room.price_day * len(date_range)

    def __str__(self):
        return f"room: {self.room} - start: {self.start} end: {self.end}"

    def __repr__(self):
        return f"booking<room: {self.room} id: {self.id}>"
