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
