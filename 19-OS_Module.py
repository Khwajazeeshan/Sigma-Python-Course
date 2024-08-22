# OS Module in Python............//////////////
import os

os.mkdir("data")  # to create a new folder/////////////

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1, 10):
    os.mkdir(f"data/day{i}")  # create a file in folder//////////

for i in range(1, 10):
    os.rename(f"data/day{i}", f"data/tutorial.png{i}")  # rename a file name in folder/////////

folder = os.listdir("data")

for folders in folder:
    print(folders)  # display a file//////////////////
print()
for folders in folder:
    print(folders)
    print(os.listdir(f"data/{folders}"))  # display a data in file////////////////////
