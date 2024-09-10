
#with open('test.txt') if the file is in the project directory.
#if somewhere else, you need the project/file path.

#with open and file.read will close the file automatically after reading it.


try:
    with open ("test.txt") as file:
        print(file.read())
except FileNotFoundError: #Add exception handling incase not found or typo.
    print("That file was not found :(")

print(file.closed) #Checks if the file is closed.
