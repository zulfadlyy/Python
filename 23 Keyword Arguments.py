# Keyword Arguments = 
# Arguments preceded by an identifier when we pass them to a function.
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

#Example of positional arguments
hello("Code","Dude","Bro") 

#Example of keyword arguments
hello(last="Code",middle="Dude",first="Bro")