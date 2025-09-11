class Car:
    make = ""
    model = ""
    year = 0
    color = ""
    engine = ""
    fuel_type = ""
    transmission = ""
    mileage = 0.0
    price = 0.0
    
my_car = Car()
my_car.make = "Toyota" 
my_car.model = "Camry"
my_car.year = 2020
my_car.color = "Blue"
my_car.engine = "2.5L I4"
my_car.fuel_type = "Gasoline"
my_car.transmission = "Automatic"
my_car.mileage = 15000.5
my_car.price = 24000.0

print(f"My car details: {my_car.year} {my_car.color} {my_car.make} {my_car.model}, Engine: {my_car.engine}, Mileage: {my_car.mileage} miles, Price: ${my_car.price}")
