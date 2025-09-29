#Duck typing = concept where the class of an object is less important than the methods/attributes it defines.
#Class type is not checked if minimum methods/attributes are present
#If it looks like a duck and quacks like a duck, it's a duck

class Duck:

    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("The chicken is walking")

    def talk(self):
        print("The chicken is clucking")

class Person:

    def catch(self, duck): #if minimum methods/attributes are present, it doesn't matter what type of object is passed
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken) #Person class doesn't care what type of object is passed as long as it has the methods walk and talk