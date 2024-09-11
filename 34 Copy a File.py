#copyfile() = copies contents of a file
#copy()     = copyfile() + permission mode + destination can be a directory
#copy2()    = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','copyfile.txt') #src,dst
shutil.copy('test.txt','copy.txt') #src,dst
shutil.copy2('test.txt','copy2.txt') #src,dst