# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
class Bus(Vehicle):
    pass

School_bus = Bus("RapidKL", 150, 300)
print(School_bus.name, School_bus.max_speed, School_bus.mileage)



