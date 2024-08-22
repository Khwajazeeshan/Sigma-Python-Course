# File Handling In Python....................//////////////////
print()

# READING FILE DATA////////////// USING FILE
f = open('myfile.txt', 'r')  # open a file.............
file = f.read()  # read file data..........
print(file)  # print file data...........
f.close()  # close file.............

# WRITING FILE DATA//////////////////// USING FILE
f = open('myfile.txt', 'w')  # Method 1 To Write data in file...........
f.write('Hello World!')
f.close()

with open('myfile.txt', 'a') as f:  # Method 2 To Write data in file...........
    f.write("\nMy Name Is Zeeshan:")

# Write-Line() Method/////////////////// USING FILE 1
f = open('myfile1.txt', 'w')
lines = ('line1\n', 'line2\n', 'line3\n')
f.writelines(lines)
f.close()

# Read-Line() Method........../////////////////// USING FILE 2
print()
f = open('myfile2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    print(f"Marks of student {i} in math is {m1}")
    print(f"Marks of student {i} in english is {m2}")
    print(line)

# Using Seek and Tell Function Method............///////////////////// USING FILE 3
print()
f = open('myfile3.txt', 'r')
f.seek(7)  # seek function is used to skip the data//////////////
print(f.tell())  # its tell the last skip value///////////////////
file = f.read()
print(file)

# Truncate Function Method////////////////// USING FILE 4
print()
f = open('myfile4.txt', 'w')
f.write("Hello World!")
f.truncate(5)
f = open('myfile4.txt', 'r')
file = f.read()
print(file)
