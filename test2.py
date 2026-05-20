import time
import sys

def basic_loading():
    print("Loading", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\nDone!")

basic_loading()
