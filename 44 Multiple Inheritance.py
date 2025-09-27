#Multiple Inheritance = when a class is derived from more than one parent class.

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

Rabbit=Rabbit()
Hawk=Hawk()
Fish=Fish()

# Rabbit.flee()
# Hawk.hunt()
# Fish.flee()
# Fish.hunt()