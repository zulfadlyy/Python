# IF statement = block of code that will execute if it's condition is TRUE.
# elif statement = means else if. similar to if statement, but used after if statement.
# else statement = used after if and elif.
# == is the equality operator compares if 2 object values are the same.
age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print(("You are a child!"))