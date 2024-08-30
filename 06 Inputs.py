name = input("What is your name?: ")
#Can't do math unless typcasted
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1
print("Hello "+name)
#Convert back the int to str to concatenate
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")