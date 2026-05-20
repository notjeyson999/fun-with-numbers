import sys
import time

def progress_bar(total_steps):
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        bar = "#" * i + "-" * (total_steps - i)
        sys.stdout.write(f"\r[{bar}] {percent:.0f}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nLoading Complete!")

progress_bar(20)
