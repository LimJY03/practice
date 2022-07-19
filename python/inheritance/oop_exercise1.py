# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
    
car = Vehicle(300, 150)
print(car.max_speed, car.mileage)

