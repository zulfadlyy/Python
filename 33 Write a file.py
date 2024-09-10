
# \n = new line
text = "Yooooooooooooo\nThis is some text\nHave a good one!\n"


# Write to a file (Creates new file)
with open('test.txt','w') as file:
    file.write(text)

# Append File (Adds new line to file)
# with open('test.txt','a') as file:
#     file.write(text)