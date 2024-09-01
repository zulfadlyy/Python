#Logical operators (AND, OR, NOT) = used to check if two or more conditional statements are TRUE.

temp = int(input("What is the temperature outside?: "))

# if temp>=0 and temp <=30:
#     print("The temperature is good today!")
#     print("Go outside!")
# elif temp < 0 or temp >30:
#     print("The temperature is bad today!")
#     print("Stay inside!")

#NOT operator just flips TRUE to FALSE and FALSE to TRUE.
if not(temp < 0 or temp >30):
    print("The temperature is good today!")
    print("Go outside!")
elif not(temp>=0 and temp <=30):
    print("The temperature is bad today!")
    print("Stay inside!")