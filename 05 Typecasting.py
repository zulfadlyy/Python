#Type Casting = convert the data type of a value to another data type
#Usually needed for concatenate

x = 1 #int
y = 2.0 #float
z = "3" #str

#Unless you type y = int(y):

print(x)
print(int(y)) #this is a temporary statement. Doesn't change the value.
print(z)

#You shouldn't do math with string
#print(z*3) will not give u 9, but 333.
#To do math you need to typecast the str, followed by the calculation statement.
z = int(z)
print(z*3)

