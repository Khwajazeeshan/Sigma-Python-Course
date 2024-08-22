# Using Time Module In Python..........//////////
import time


def whileloop():
    i = 0
    while i < 10000:
        i = i + 1
        print(i)


def forloop():
    for i in range(10000):
        print(i)


init = time.time()  # It returns the current time in floating poit.
whileloop()
t1 = time.time() - init
forloop()
t2 = time.time() - init
print(t1)
print(t2)

# Using Time Sleep Function.............
print("Hello World")
time.sleep(3)  # it stops the execution for specific time
print("this is printed after 3 seconds")

# Using Strftime Function................
t = time.localtime()
format_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(format_time)
