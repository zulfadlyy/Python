#Multi-level Inheritance = when a derived(child) class inherits another derived(child) class.
#Its like a Family Tree
class Organism: #Grandparent class

    alive = True

class Animal(Organism): #Parent class

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #Child class

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive) #Inherited from organism class
dog.eat()
dog.bark()