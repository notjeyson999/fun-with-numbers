import threading
import time

def loading_animation(stop_event):
    animation = ["Loading.  ", "Loading.. ", "Loading..."]
    idx = 0
    while not stop_event.is_set():
        print("\r" + animation[idx], end="")
        idx = (idx + 1) % len(animation)
        time.sleep(0.3)
    print("\rLoading... Done!   ")
    time.sleep(0.4)
    print()


def process_number(number, result):
    # Positive / Negative / Zero
    if number > 0:
        result.append(f" {GREEN}Positive")
    elif number < 0:
        result.append(f" {RED}Negative")
    else:
        result.append(f" {GREY}Zero")

    # Odd or Even
    if number % 2 == 0:
        result.append(f" {GREEN}Even")
    else:
        result.append(f" {RED}Odd")

    # Factors
    factors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)
    result.append(f" {YELLOW}Factors are {RED}" + " ".join(map(str, factors)))

    # Prime check
    if number > 1 and len(factors) == 2:
        result.append(f" {GREEN}Is a prime number")
    else:
        result.append(f" {RED}Is not a prime number")

    # Binary / Hex / Octal
    result.append(f" {YELLOW}Binary: {RED}{bin(number)[2:]}")
    result.append(f" {YELLOW}Hexadecimal: {RED}{hex(number)[2:]}")
    result.append(f" {YELLOW}Octal: {RED}{oct(number)[2:]}")


def number_features():
    """Displays features of the number entered"""
    global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER

    while True:
        clear_screen()

        try:
            number = int(input(f"{MAGENTA}Please enter a whole number that can be checked over: {CYAN}"))
        except ValueError:
            print(f"{RED}Please input an integer")
            print(f"{YELLOW}Press enter to return to main menu")
            input()
            break

        # Storage for results
        result = []

        # Start loading animation
        stop_event = threading.Event()
        loader = threading.Thread(target=loading_animation, args=(stop_event,))
        loader.start()

        # Start number processing
        worker = threading.Thread(target=process_number, args=(number, result))
        worker.start()

        # Wait for processing to finish
        worker.join()

        # Stop loading animation
        stop_event.set()
        loader.join()

        # Display results
        print(f"{YELLOW}The features of {RED}{number} {YELLOW}are:")
        for line in result:
            print(line)

        # Update global stats
        if NUMBER_COUNT == 0:
            SMALLEST_NUMBER = number
            LARGEST_NUMBER = number
        else:
            SMALLEST_NUMBER = min(number, SMALLEST_NUMBER)
            LARGEST_NUMBER = max(number, LARGEST_NUMBER)

        NUMBER_COUNT += 1
        NUMBER_TOTAL += number

        # Ask to repeat
        again = input(f"{MAGENTA}Do you want to check another number (y/n)?: {CYAN}").lower()
        if again != "y":
            print(f"{MAGENTA}Press Enter to return to main menu")
            input()
            break
number_features()
