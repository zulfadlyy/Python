#Slicing used to create a substring by extracting elements from another string.
#               indexing[] or slice()
#               [start:stop:step]

name = "Zack Farsley"
#        can use [:4] also
first_name = name[0:4] #first starting index inclusive, last ending is exclusive.
last_name = name [5:12]
#        can use [5:] also
funky_name = name[0:12:2]
#        can use [::2] also
reversed_name = name [::-1]


print (first_name)
print (last_name)
print (funky_name)
print (reversed_name)

website = "http://google.com"

trimthefat = slice(7,-4)

print(str.capitalize(website[trimthefat]))
