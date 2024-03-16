from datetime import datetime, timedelta

class BookingPriceCalculator:
  def __init__(self, price, period):
    self.price = price
    self.period = period
  
  def calculate(self):
      date_range = [date for date in self.period.range(timedelta(days=1))]
      return self.price * len(date_range)