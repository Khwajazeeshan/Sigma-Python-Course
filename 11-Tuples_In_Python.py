# Tuples in Python..................!!!!!!!!!!!!!!!!
print()
tup = (1, 3, 56, 99, "Hello", True)
print(type(tup), tup)
tup2 = tup[1:5]
print(tup2)
res = tup.count(3)
print(res)
res = len(tup)
print(res)

# Manipulating Tuple..............!!!!!!!!!!
print("\n")
countries = ("Pakistan", "spain", 'saudia', "USA", "Iran")
print(countries)
temp = list(countries)  # convert tuple into list
temp.append("Russia")  # add item
temp.pop(1)  # remove item
temp[2] = "sudan"  # change item
countries = tuple(temp)  # convert list into tuple
print(countries)

