'''Recreation of the original Fun with Numbers''' 
#Devoloped by Jeyson Blain :P

#Imports required libraries
import os

#State global variables
NUMBER_COUNT = 0
NUMBER_TOTAL = 0
SMALLEST_NUMBER = 0
LARGEST_NUMBER = 0
PLOT_COUNT = 0


def main():
    '''The main menu'''
    #Sets the exit condition to false
    load_stats()
    exit_flag = False

    while not exit_flag:
        clear_screen()
        print("Welcome to the Fun with Numbers!")
        print("Choose from the menu below:")
        print(" (A) Check number features")
        print(" (B) Plot numbers")
        print(" (C) Check overall stats")
        print("\n (X) Save and exit")
        choice = input("Choice: ").upper()

    #Takes user input and opens sub routines
        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            stats()
        elif choice == "X":
            save_stats()
            exit_flag = True

def number_features():
    """Displays features of a number"""
    clear_screen()
    global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER
    number = int(input("Please enter a whole number that can be checked over: "))
    print(f"The features of {number} are...")

    #Check if the number is odd or even
    if number < 0:
        print(" Positive")
    elif number < 0:
        print(" Negative")
    else:
        print(" Zero")

    #Check if the number is odd or even
    if number % 2 == 0:
        print(" Even")
    else:
        print(" Odd")

    #Lists all the factors of the number
    print(" Factors are", end="")
    factor_count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            print(" " + str(i), end="")
            factor_count += 1

    #Check if number is a prime
    if factor_count == 2:
        print("\n Is a prime number")
    else:
        print("\n Is not a prime number")
    input()

    #Update global variables
    if NUMBER_COUNT == 0:
        SMALLEST_NUMBER == number
        LARGEST_NUMBER == number
    else:
        SMALLEST_NUMBER = min(number, SMALLEST_NUMBER)
        LARGEST_NUMBER = max(number, LARGEST_NUMBER)

    NUMBER_COUNT += 1
    NUMBER_TOTAL += number

def draw_graph(table):
    """Draws the graph for the plotter routine"""
    print("                                                     x axis")
    print("     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38")
    print("  --------------------------------------------------------------------------------------------------------------------")
    for i, row in enumerate(table, start=1):
        print(f"{i:2}|  {'  '.join(row)} |")
    print("  --------------------------------------------------------------------------------------------------------------------")


def plotter():
    """Plot x and y cords on a table"""
    clear_screen()
    #Creates a blank table with specified rows and columns
    global PLOT_COUNT
    num_columns = 38
    num_rows = 12
    table = [[" " for column in range(num_columns)] for row in range(num_rows)]
    draw_graph(table)
    print("Enter a coordinate below to be added to the plot")
    while True:
        try:
            x_axis = int(input("x axis: "))
            if 0 < x_axis <= num_columns:
                y_axis = int(input("y axis: "))
                if 0 < y_axis <= num_columns:
                    clear_screen()
                    PLOT_COUNT += 1
                    table[y_axis - 1] [x_axis - 1] = "x"
                    if 0 < x_axis <= num_rows:
                        draw_graph(table)
                        another_cord = input("Do you wish to add another coordinate (y/n)? ").lower()
                        if another_cord == 'n':
                            break
                else:
                    pass
            else:
                pass
        except ValueError:
            print("Invalid input. Please use integers.")

def stats():
    """Show statistics about numbers used in app"""
    clear_screen()
    print("Here are your statistics of overall use:")
    print(f" Numbers entered:  {NUMBER_COUNT}")
    print(f" Total of numbers:  {NUMBER_TOTAL}")
    print(f" Average of Numbers:  {NUMBER_TOTAL / NUMBER_COUNT}")
    print(f" Smallest number entered:  {SMALLEST_NUMBER}")
    print(f" Largest Number entered:  {LARGEST_NUMBER}")
    input()

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def save_stats():
    """Saves statistics from current session to file"""
    with open('stats.txt', 'w', encoding='utf8') as f:
        f.write(f"{NUMBER_COUNT}\n")
        f.write(f"{NUMBER_TOTAL}\n")
        f.write(f"{SMALLEST_NUMBER}\n")
        f.write(f"{LARGEST_NUMBER}\n")
        f.write(f"{PLOT_COUNT}\n")

def load_stats():
    """Loads statistics from previous session"""
    try:
        with open('stats.txt', 'r') as f:
            global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER, PLOT_COUNT
            NUMBER_COUNT = int(f.readline())
            NUMBER_TOTAL = int(f.readline())
            SMALLEST_NUMBER = int(f.readline())
            LARGEST_NUMBER = int(f.readline())
            PLOT_COUNT = int(f.readline())
    except FileNotFoundError:
        NUMBER_COUNT = 0
        NUMBER_TOTAL = 0
        SMALLEST_NUMBER = 0
        LARGEST_NUMBER = 0
        PLOT_COUNT = 0

main()