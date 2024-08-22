# Using List In Python...............!!!!!!!!!!!!!!!!
print()

l = [1, 2, 3, 4, 5, 6, "Hello", True]

print(l, "\n")
print(l[0])
print(l[2])
print(l[4])

print()
print(len(l))
print(type(l))
print(l[1:7])
print(l[1:8:2])

# List Comprehension.......!!!!!!!
print()
l = [i * i for i in range(6)]
print(l)
l = [i * i for i in range(10) if i % 2 == 0]
print(l)

# List Method In Python.........!!!!!!!!!!!!!!!!
print()
l = [33, 45, 1, 2, 1, 3, 4, 1, 5, 78]
print(l)
print()
l.append(52)  # it is used to put value in end of list......
print(l)
l.sort()
print(l)
l.sort(reverse=True)  # it is use for sorting.........
print(l)
l.reverse()  # it is use for reversing of list........
print(l)
print(l.index(1))  # to display the value on index.........
print(l.count(1))  # it is used for counting same value............

m = [700, 800, 900]  # extend of list two with list one.......
l.extend(m)

k = l + m  # concatenating of two list
print(k)
