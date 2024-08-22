# Using Asyncio Module In Python........../////////////////
"""
The asyncio module in Python helps you write programs that can do multiple things at the same time,
without getting stuck waiting for one task to finish before moving on to the next
"""
import asyncio


async def func1():
    await asyncio.sleep(3)
    print("func 1")


async def func2():
    await asyncio.sleep(3)
    print("func 2")


async def func3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    results = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print(results)
asyncio.run(main())