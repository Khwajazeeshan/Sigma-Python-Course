# Dictionaries and Methods In Python..........!!!!!!!!!!!!
print()
dic = {
    101: "ALi",
    102: "Ahmed",
    103: "asad",
    104: "ammer",
    105: "ahad",
    106: "Sabtain",
    107: "zeeshan",
    108: "usman",
    109: "saqib",
    110: "tayyab",
}
print(dic[107])

print()
info = dict(name='zeeshan', age=20, eligible=True)
print(info)
for key in info.keys():
    print(f"The Value Corresponding to key {key} is {info[key]}")

# Dictionaries Methods.............!!!!!!!!!!!!!!!!!
print("\n\t*****Dictionaries Methods*****\n")
ep1 = {101: 34, 102: 45, 103: 55, 104: 66, 105: 74, 106: 89}
ep2 = {107: 83, 108: 46, 109: 61, 110: 59}

ep1.update(ep2)
# ep1.clear()
ep1.pop(102)
ep1.popitem()   # Remove last  item
del ep1[107]
print(ep1)
