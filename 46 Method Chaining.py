#Method Chaining =  calling multiple methods sequentially
#Each cell performs an action on the same object and returns the object itself.

class Car:

    def turn_on(self):
        print("You start the engine")
        return self #Return the object itself to allow method chaining
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brake")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
        
car = Car() #Create an object of the Car class
#Normal way of calling methods:
# car.turn_on
# car.drive()
# car.turn_off()

#Method Chaining way of calling methods:
# car.turn_on().drive().brake().turn_off()

#Cleaner way of method chaining:
#Backslash (\) allows you to break a single statement into multiple lines for better readability.
car.turn_on()\
   .drive()\
   .brake()\
   .turn_off()