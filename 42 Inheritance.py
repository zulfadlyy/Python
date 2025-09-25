# Parent (base) class
class Animal:
    # Class attribute shared by all animals
    alive = True

    # Method: all animals can eat
    def eat(self):
        print("This animal is eating")

    # Method: all animals can sleep
    def sleep(self):
        print("This animal is sleeping")


# Child (derived) class: Rabbit
class Rabbit(Animal):
    # Inherits 'alive', 'eat()', and 'sleep()' from Animal
    # Adds its own unique behavior: run()
    def run(self):
        print("This rabbit is running")


# Child (derived) class: Fish
class Fish(Animal):
    # Inherits 'alive', 'eat()', and 'sleep()' from Animal
    # Adds its own unique behavior: swim()
    def swim(self):
        print("This fish is swimming")


# Child (derived) class: Hawk
class Hawk(Animal):
    # Inherits 'alive', 'eat()', and 'sleep()' from Animal
    # Adds its own unique behavior: fly()
    def fly(self):
        print("This hawk is flying")


# -------------------------
# Create objects (instances)
# -------------------------
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# Call subclass-specific methods
rabbit.run()   # Calls Rabbit's run() method
fish.swim()    # Calls Fish's swim() method
hawk.fly()     # Calls Hawk's fly() method

# You can also use inherited methods from Animal:
# print(rabbit.alive)  # Prints True (inherited from Animal)
# fish.eat()           # Prints "This animal is eating"
# hawk.sleep()         # Prints "This animal is sleeping"