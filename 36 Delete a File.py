import os

# path = "remove.txt" or "36 Delete a Folder"

#To remove a file
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that!")
# else:
#   print(path+" was deleted")

# To remove a folder (Empty Directory)
# try:
#     os.rmdir(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that!")
# else:
#   print(path+" was deleted")

# To remove folder that contains files (DANGEROUS)
import shutil
# try:
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that!")
# else:
#   print(path+" was deleted")