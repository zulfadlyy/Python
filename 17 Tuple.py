# Tuple = collection which are ORDERED and UNCHANGEABLE
#         used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro")) #How many times str() appear
print(student.index("male")) #Which index number is str()

for x in student: 
    print(x) #Prints contents of the tuple

if "Bro" in student: #Search for str in tuple
    print("Bro is here!")