import os

source = "move.txt"
destination = "C:\\Users\\blazi\\Documents\\VSCODE\\Python-1\\35 Move a File\\move.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")