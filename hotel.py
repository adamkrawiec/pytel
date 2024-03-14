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
        Booking.id += 1
        self.id = Booking.id
        Booking.bookings.append(self)