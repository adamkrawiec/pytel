from datetime import datetime, timedelta
from datetimerange import DateTimeRange

class Hotel:
    id = 0
    def __init__(self, name):
        self.name = name
        Hotel.id += 1
        self.id = Hotel.id

    def __str__(self):
        return f"name: {self.name}"
    
    def __repr__(self):
        return f"hotel<name: {self.name}>"

    def rooms(self):
        return [room for room in Room.rooms if room.hotel == self]

    def rooms_available(self, start, end):
        return [room for room in self.rooms() if not room.is_booked_between(start, end)]


# class RoomRepository(object):
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(RoomRepository, cls).__new__(cls)
#         return cls._instance
    
#     def __init__(self):
#         self.current_id = 0
#         self.rooms = []
    
#     def add_room(self, room):
#         self.current_id += 1
#         room.id = self.current_id
#         self.current_id += 1
#         self.rooms.append(room)  

class Room:
    id = 0
    rooms = []

    @classmethod
    def all(cls):
      return cls.rooms

    def __init__(self, hotel):
        self.hotel = hotel
        Room.id += 1
        self.id = Room.id
        Room.rooms.append(self)
    
    def bookings(self):
        return [booking for booking in Booking.bookings if booking.room == self]
  
    def book(self, start, end):
        if self.is_booked_between(start, end):
            raise ValueError("Room is already booked for this date range")
        return Booking(self, start, end)
  
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
