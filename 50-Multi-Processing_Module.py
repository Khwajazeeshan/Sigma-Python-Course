# Using Multi-Processing Module In Python.............////////////
"""
The multiprocessing module in Python as a way to do multiple things at the same time using separate "workers"
that run independently. It's like having several people working on different tasks simultaneously.
This can make your program run faster.This is like Multi-Threading Module.
"""
import multiprocessing
import requests


def download(myweb, name):
    print(f"Start Downloading{name}")
    result = requests.get(myweb)
    open(f"pics/file{name}.jpg", "wb").write(result.content)


if __name__ == "__main__":
    myweb = "https://picsum.photos/200/300"

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=download, args=(myweb, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All downloads finished.")
