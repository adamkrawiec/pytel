class BookingRepository:
    _instance = None
    _bookings = []
    _booking_id = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BookingRepository, cls).__new__(cls)
        return cls._instance

    def persist(self, booking):
        booking.id = self._booking_id
        self._booking_id += 1
        self._bookings.append(booking)
        return booking
    
    def find(self, id):
        return next((booking for booking in self._bookings if booking.id == id), None)
    
    def all(self):
      return self._bookings
    
    def delete_all(self):
      self._bookings = []