# Scope = The region that a variable is recognized.
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.


#Example of local scope
def display_name():
    name = "Local" #Local scope because it is declared INSIDE of a function.
    print(name) # Only available inside this function

display_name()

#Example of global scope
name = "Global" #Global scope (available inside & outside functions)
print(name)

# If your local scope has a local and global variable, it will use the local first.
# The order python uses it's variables are as follows:
#   Local
#   Enclosing
#   Global
#   Built-in