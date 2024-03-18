import unittest
from hotel.hotel import Hotel
from hotel.room import Room
from hotel.booking import BookingRepository
from datetime import datetime

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Ritz")
        self.hotel2 = Hotel("Hilton")
        self.room = Room(self.hotel, 100)
        self.room2 = Room(self.hotel, 200)
        self.room3 = Room(self.hotel2, 200)
        self.booking = self.room.book(datetime(2021, 1, 1), datetime(2021, 1, 10))
        self.booking2 = self.room.book(datetime(2021, 1, 20), datetime(2021, 1, 30))
        self.booking3 = self.room2.book(datetime(2021, 1, 10), datetime(2021, 1, 30))

    def tearDown(self):
        BookingRepository().delete_all()

    def test_rooms(self):
        """Returns rooms asigned to the hotel"""
        self.assertEqual(self.hotel.rooms(), [self.room, self.room2])
  
    def test_rooms_available(self):
        """Returns rooms available for a date range"""
        self.assertEqual(self.hotel.rooms_available(datetime(2021, 1, 12), datetime(2021, 1, 15)), [self.room])

if __name__ == '__main__':
    unittest.main()