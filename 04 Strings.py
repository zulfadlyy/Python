#These are some of the things you can do with Strings
#1 Len short for length.

name = "bro Code"
number = "123"
mixed = "abc123"
#This will print 8 as spaces are also counted.
print(len(name))

#2 .find returns the quantity of the searched text.

#This find the letter "o" and returns 2.
print(name.find("o"))

#Capitalize 1st Letter
print(name.capitalize())

#Uppercase the whole word
print(name.upper())

#Lowercase the whole word
print(name.lower())

#Check if STR is a number
print(name.isdigit())
print(number.isdigit())

#Combination will result in FALSE
print(mixed.isdigit())

#Check if STR is an Alphabet
print(name.isalpha())

#Count (arguement)
print(name.count("o"))

#Find and Replace (from , to)
print(name.replace("o","a"))

#MultiplePrint
print(name*3)
