# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"


# The normal example
#print("The "+animal+" jumped over the "+item)

# Using str.format()
#   Using Values    
# print("The {} jumped over the {}".format("cow","moon"))

#   Using Variables
# print("The {} jumped over the {}".format(animal,item))

#   Positional Argument
# print("The {1} jumped over the {0}".format(animal,item))

#   Keyword Argument
# print("The {ani} jumped over the {itm}".format(ani="cow",itm="moon"))

#   String that you would like to format into a variable
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

#   Padding
name = "Bro"
print("Hello, my name is {}. Nice to meet you".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
#       Left Align
print("Hello, my name is {:<10}. Nice to meet you".format(name))

#       Right Align
print("Hello, my name is {:>10}. Nice to meet you".format(name))

#       Center Align
print("Hello, my name is {:^10}. Nice to meet you".format(name))

#   Format Numbers
number = 1000

#   Display decimal place (2 decimal, f being float. This will round your number.)
print("The number pi is {:.2f}".format(number))

#   Number in comma (1,000)
print("The number pi is {:,}".format(number))

#   Number in Binary (1111101000)
print("The number pi is {:b}".format(number))

#   Number in Octal (1750)
print("The number pi is {:o}".format(number))

#   Number in Hexadecimal (3E8)
print("The number pi is {:x}".format(number))

#   Number in Scientific Notation (1.000000E+03)
print("The number pi is {:E}".format(number))


