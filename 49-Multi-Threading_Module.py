# Using Multi-Threading Module In Python...............//////////////////
"""
Multithreading in Python refers to the capability of a program to execute multiple
threads concurrently within a single process.
"""

import threading
import time

def func(seconds):
    print(f"the seconds is {seconds}")
    time.sleep(seconds)
    print(f"\nhello World!{seconds}")


t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()

t1.join()
t2.join()
print("\nProgram Complete")