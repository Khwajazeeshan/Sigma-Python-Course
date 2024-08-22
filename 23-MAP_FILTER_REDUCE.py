# Using Map, Filter, Reduce In Python.............//////////////////
print()
# USING MAP METHOD///////////////////
l = [2, 4, 6, 3, 8, 9, 5, 1]
newl = list(map(lambda x: x * x * x, l))
print(newl)

# USING FILTER METHOD///////////////////
print()
l1 = [4, 7, 53, 99, 10, 12, 34, 2, 1, 3, 1, 5]
newl1 = list(filter(lambda x: x > 5, l1))
print(newl1)

# USING REDUCE METHOD//////////////////
print()
from functools import reduce

l2 = [2, 4, 6, 5, 6, 7, 4, 3, 8, 9, 5]
newl2 = reduce(lambda x, y: x + y, l2)
print(newl2)
