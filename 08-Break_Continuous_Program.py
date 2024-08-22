# using break and continuous statement...........!!!!!!!!!!!!!

# using break statement..............
print()
for i in range(10):
    if i == 8:
        break
    print("5 X", i + 1, "=", 5 * (i + 1))

print("\n****outside loop****\n\n")

# using continuous statement...........
for i in range(10):
    if i == 8:
        print("\tSkip\t\t")
        continue
    print("5 X", i + 1, "=", 5 * (i + 1),)
