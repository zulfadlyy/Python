from car import Car


car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

#Class Variable "wheel = 4" (from car.py)
#However, if you define it again..It will overwrite.

car_2.wheels = 2

print(car_1.wheels)
print(car_2.wheels)