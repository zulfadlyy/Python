# A Variable is a container for a value.
# It behaves as the value that it contains.
#String (Text Characters)
name = "Bro"
print(name)

# You can concatenate text and string OR Integer and Float.
print("Hello "+ name)

# You can check the data type
print(type(name))

#If you have 2 word variable, seperate with _
first_name = "Zack"
last_name = "Farsley"

#Adding spaces you need to add it between the ""
full_name = first_name + " " + last_name
print(full_name)

#Integer (Whole Numbers)
age = 30

#Code will always follow the latest entry
#age = age + 1 or you can use
age += 1
print (age)

#age is a Int data type
print(type(age))

#Typecasting allows you to change the data type of a variable from its original to concatenate
#Below is STR + typcasted INT
print("Your age is: "+(str(age)))

#Float (Decimal Numbers)
height = 250.5
print("Your height is: "+ (str(height))+"cm")
print(type(height))

#Boolean (TRUE or FALSE)
human = False
print("Are you a human: "+(str(human)))
print(type(human))