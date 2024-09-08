import os
#\ must use \\ for PATH
path = "C:\\Users\\blazi\\Documents\\VSCODE\\File Detection\\folder"

#   Checks if that file or location exist.
if os.path.exists(path):
    print("That location exists!")
#   Checks if that PATH is a file
    if os.path.isfile(path):
        print("That is a file!")
#   Checks if that PATH is a directory
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")



