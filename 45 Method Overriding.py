#Method Overriding is a feature of OOP that allows a subclass or child class to provide a specific implementation of a method that is already defined in its superclass or parent class.

class Animal: #Parent class

    def eat(self): #Method of parent class
        print("Animal is eating")

class Rabbit(Animal): #Child class
    def eat(self): #Overriding the method of parent class
        print("The rabbit is eating a carrot")


rabbit = Rabbit() #Create an object of the child class
rabbit.eat() #Call the method from the parent class

#Rabbit class has overridden the eat() method of the Animal class.