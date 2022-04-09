import os
import random
import string
import time

os.system("clear")
pool = random.choices(string.ascii_letters, k=15)
starting_time = time.perf_counter()

while pool:
    print(", ".join(pool))
    zadani = input("ktere písmeno chceš vyhodit? ")

    if zadani in pool:
        pool.remove(zadani)
        print(", ".join(pool))
    else:
        print(zadani, "není součástí písmen!")
    os.system("clear")

else:
    print("Seznam je prázdný!")
    ending_time = time.perf_counter()
    resulted_time = time.strftime('%S', time.gmtime(ending_time - starting_time))
    print("Tvůj čas:", resulted_time, "vteřin.")
