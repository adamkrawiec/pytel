require("date")

class Hotel
  attr_reader :id, :name, :rooms

  @@id = 0
  def initialize(name)
    @id = @@id += 1
    @name = name
  end

  def rooms
    Room.select { _1.hotel == self }
  end

  def rooms_available_between(start_date, end_date)
    rooms.reject { _1.booked_between?(start_date, end_date) }
  end
end

class Room
  attr_reader :id, :hotel

  @@id = 0
  def initialize(hotel)
    @id = @@id += 1
    @hotel = hotel
  end

  def book(start_date, end_date)
    return if booked_between?(start_date, end_date)

    Booking.new(room: self, start_date: start_date, end_date: end_date)
  end

  def booked_on?(date)
    bookings.any? { _1.period.include?(date) }
  end

  def booked_between?(start_date, end_date)
    (start_date...end_date).any? { booked_on?(_1) }
  end

  def bookings
    Booking.all.select { _1.room  == self }
  end
end

class Booking
  attr_reader :id, :room, :start_date, :end_date

  @@id = 0
  @@bookings = []

  def self.all
    @@bookings
  end

  def initialize(room:, start_date:, end_date:)
    @id = @@id += 1
    @room = room
    @start_date = start_date
    @end_date = end_date
    @@bookings << self
  end

  def period
    (start_date..end_date)
  end

end
#  require("./hotel")
hotel = Hotel.new("Ritz")
room1 = Room.new(hotel)
room2 = Room.new(hotel)

room1.book(Date.new(2021, 1, 1), Date.new(2021, 1, 10))
room1.book(Date.new(2021, 1, 20), Date.new(2021, 1, 30))

room1.booked_on?(Date.new(2021, 1, 5)) # true
room1.booked_on?(Date.new(2021, 1, 15)) # false

room1.booked_between?(Date.new(2021, 1, 5), Date.new(2021, 1, 7)) # true
room1.booked_between?(Date.new(2021, 1, 5), Date.new(2021, 1, 15)) # true
room1.booked_between?(Date.new(2021, 1, 12), Date.new(2021, 1, 15)) # false
room1.booked_between?(Date.new(2021, 1, 15), Date.new(2021, 2, 1)) # true