# Using While Loop.....!!!!!

i = 0
while i <= 10:
    # i = int(input("enter number\n"))
    print(i)
    i = i + 1
print("task complete\n")

# Else with while loop.......!!!!!!!!
count = -5
while count > 0:
    print(count)
    count = count - 1
else:
    print("\ni am outside of loop")

# Else In Loop...........////////////////
print("\n\t***** Else In Loop *****\n")
i = 0
while i < 7:
    print(i)
    i = i + 1
    if i == 4:
        break

else:
    print("outside of Loop ")
