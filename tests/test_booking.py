import unittest
from hotel.hotel import Hotel
from hotel.room import Room
from hotel.booking import Booking, BookingRepository
from datetime import datetime

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = Booking(Room(Hotel("Ritz"), 10), datetime(2021, 1, 1), datetime(2021, 1, 10))

    def tearDown(self):
        BookingRepository().delete_all()
        
    def test_price(self):
        """Returns the price of the booking"""
        self.assertEqual(self.booking.price(), 100)

if __name__ == '__main__':
    unittest.main()