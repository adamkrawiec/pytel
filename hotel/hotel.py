from .room import Room

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

# from hotel.booking import Booking
# from hotel.hotel import Hotel
# from hotel.room import Room
# import datetime
# h = Hotel("ritz")
# r = Room(h, 100)
# b = Booking(r, datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 10))