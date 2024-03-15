import unittest
import hotel
from datetime import datetime

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = hotel.Hotel("Ritz")
        self.hotel2 = hotel.Hotel("Hilton")
        self.room = hotel.Room(self.hotel)
        self.room2 = hotel.Room(self.hotel)
        self.room3 = hotel.Room(self.hotel2)
        self.booking = self.room.book(datetime(2021, 1, 1), datetime(2021, 1, 10))
        self.booking2 = self.room.book(datetime(2021, 1, 20), datetime(2021, 1, 30))
        self.booking3 = self.room2.book(datetime(2021, 1, 10), datetime(2021, 1, 30))

    def test_rooms(self):
        """Returns rooms asigned to the hotel"""
        self.assertEqual(self.hotel.rooms(), [self.room, self.room2])
  
    def test_rooms_available(self):
        """Returns rooms available for a date range"""
        self.assertEqual(self.hotel.rooms_available(datetime(2021, 1, 12), datetime(2021, 1, 15)), [self.room])

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.hotel = hotel.Hotel("Ritz")
        self.room = hotel.Room(self.hotel)
        self.room2 = hotel.Room(self.hotel)
        self.booking = self.room.book(datetime(2021, 1, 1), datetime(2021, 1, 10))
        self.booking2 = self.room.book(datetime(2021, 1, 20), datetime(2021, 1, 30))
        self.booking3 = self.room2.book(datetime(2021, 1, 10), datetime(2021, 1, 30))

    def test_book(self):
        """Books a room for a date range"""
        book = self.room.book(datetime(2021, 1, 12), datetime(2021, 1, 15))
        self.assertIn(book, self.room.bookings())

        with self.assertRaises(ValueError):
            self.room.book(datetime(2021, 1, 5), datetime(2021, 1, 8))

    def test_bookings(self):
        """Returns bookings for the room"""
        self.assertEqual(self.room.bookings(), [self.booking, self.booking2])

    def test_is_booked_on(self):
        """Returns True if the room has a booking for a date"""
        self.assertTrue(self.room.is_booked_on(datetime(2021, 1, 5)))
        self.assertFalse(self.room.is_booked_on(datetime(2021, 1, 15)))

    def test_is_booked_between(self):
        """Returns True if the room is booked between a date range"""
        self.assertTrue(self.room.is_booked_between(datetime(2021, 1, 2), datetime(2021, 1, 5)))
        self.assertTrue(self.room.is_booked_between(datetime(2021, 1, 2), datetime(2021, 1, 15)))
        self.assertFalse(self.room.is_booked_between(datetime(2021, 1, 12), datetime(2021, 1, 15)))

if __name__ == '__main__':
    unittest.main()