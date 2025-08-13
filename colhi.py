
class Vehicle:
  def __init__(self, capacity):
    self.capacity = capacity

  def fare(self):
    return self.capacity * 100

# Child class
class Bus(Vehicle):
  pass # Inherits everything from Vehicle

# Create a Bus object
bus = Bus(50)

# Print the fare
print("Total Bus Fare:", bus.fare())