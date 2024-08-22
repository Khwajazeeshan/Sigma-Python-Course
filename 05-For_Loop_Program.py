# For Loop Program.....!!!!!!!!!

x = ["zeeshan", "asad"]

for i in x:
    print(i)
    for j in i:
        print(j)

print("\n\n")
for z in range(1, 21, 8):
    print(z)

# Else In Loop.............///////////////
print("\n\t**** Else In Loop *****\n")
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop Break")
