
class Car:

    color = None # class variable

class Motorcycle:

    color = None 

def change_color(vehicle, color): # Function not within a class that takes an object as an argument

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

# Call the function and pass in an object and a color
change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

