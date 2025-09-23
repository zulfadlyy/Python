# This .py file demonstrates class (named "Car") definitition
# You can use a seperate .py file to store classes if you have many.
# Otherwise, in the same .py file as the code is also fine.


# class <class name>:
class Car:

    wheels = 4 #This is a class variable (acts as the default)
    
    #__init__ is a special method in Python classes that auto runs when new object(s) from the class are created.
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    #f-strings are used to combine expressions with string.
    def drive(self):
        print(f"This {self.year} {self.color} {self.make} {self.model} is driving.")

    
    def stop(self):
        print(f"This {self.year} {self.color} {self.make} {self.model} is stopped.")