# Using Sets And Sets Method In Python..........!!!!!!!!!!
print()
set = {2, 4, 6, 5, 3, 7, 8, 5, 2, 9, }
print(type(set), set)

s = {"ali", 2, 5, True, 8, 9.5, False}
print(s)
print()
for value in s:
    print(value)

# Set Methods............///////////////
print("\t\t*****SET METHODS*****\n")
s1 = {1, 2, 3, 5}
s2 = {2, 3, 4, 7, 8}
print(s1.union(s2))  # It displays same value only one time
s1.update(s2)  # it displays both value
print(s1, s2)
print()
s3 = {3, 4, 6, 7, 8}
s4 = {3, 4, 6, 1, 2}
print(s3.intersection(s4))  # it displays the same value in both side
print(s3.symmetric_difference(s4))  # it displays value which not same on both side
print()
print(s3.isdisjoint(s4))  # if value same on b/s it returns false otherwise true
s6 = {3, 4, 6}
print(s3.issuperset(s6))  # if set3  value in set6 it returns true otherwise false
print(s6.issubset(s3))  # if s6 value in s3 it returns true otherwise false
print()
s3.add(10)  # it adds value in set
print(s3)
s4.remove(1)  # it removes value in set
print(s4)
item = s3.pop()  # it pops value in set
print(item)
s3.clear()  # it clears all value in set
print(s3)
