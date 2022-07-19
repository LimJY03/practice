class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    type = 'bus'
    transport = 'public transport'

class Car(Vehicle):
    type = 'car'
    transport = 'private transport'

bus = Bus('RapidKL', 150, 80)
car = Car('Audi Q5', 240, 105)

dict_bus = {
    'Color': bus.color,
    'Vehicle_name': bus.name,
    'Speed': bus.max_speed,
    'Mileage': bus.mileage,
    'Type': bus.type,
    'Transport': bus.transport

}

dict_car = {
    'Color': car.color,
    'Vehicle_name': car.name,
    'Speed': car.max_speed,
    'Mileage': car.mileage,
    'Type': car.type,
    'Transport': car.transport
}
print(dict_bus)
print(dict_car)


