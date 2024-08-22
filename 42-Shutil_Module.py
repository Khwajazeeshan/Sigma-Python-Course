# Using Shutil Module In Python.............///////////////

import shutil

# Its Used when copy a file.
shutil.copy("welcome.py", "main.py")  # create new file "main" and copy data from "welcome" file.

# Its Used when copy a folder.
shutil.copytree("data", "data1")  # create new folder "data1" and copy data from "data" folder.

# It's used to move file from folder to outside the folder.
shutil.move("data/tutorial.png7", "file.file")