# Using Function Caching in Python..........////////////
"""
When you call a cached function with certain inputs, the library remembers the results for those inputs. If you call the
function again with the same inputs, it returns the saved result directly, without doing all the work again.
"""
from functools import lru_cache
import time


@lru_cache()
def fx(n):
    time.sleep(3)
    return n * 4


print(fx(10))
print("done for 10")
print(fx(15))
print("done for 15")
print(fx(25))
print("done for 25")

print(fx(10))
print("done for 10")
print(fx(15))
print("done for 15")
print(fx(30))
print("done for 25")