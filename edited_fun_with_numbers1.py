'''Recreation of the original Fun with Numbers''' 
#Devoloped by Jeyson Blain :P

#Imports required libraries
import os
#Imports time function
import time
#Imports random for higher or lower feature
import random

#States Colours for UI
RESET   = '\033[0m'  #Sets to default#
RED     = '\033[31m' #Special Characters#
GREEN   = '\033[32m' #Choices#
YELLOW  = '\033[33m' #Text#
CYAN    = '\033[36m' #Input#

#State global variables
NUMBER_COUNT = 0
NUMBER_TOTAL = 0
SMALLEST_NUMBER = 0
LARGEST_NUMBER = 0
PLOT_COUNT = 0
TOTAL_GUESSES = 0
TOTAL_INVALID_GUESSES = 0
CORRECT_GUESSES = 0

def main():
    '''The main menu'''
    #Sets the exit condition to false
    load_stats()
    exit_flag = False

    while not exit_flag:
        clear_screen()
        print(f"{CYAN}Welcome to the Fun with Numbers!")
        print(f"Choose from the menu below:{RESET}")
        print(f" {GREEN}(A){RESET} {YELLOW}Check number features")
        print(f" {GREEN}(B){RESET} {YELLOW}Plot numbers")
        print(f" {GREEN}(C){RESET} {YELLOW}Higher or Lower")
        print(f" {GREEN}(D){RESET} {YELLOW}Check overall stats")
        print(f"\n {GREEN}(X){RESET} {YELLOW}Save and exit")
        choice = input(f"{GREEN}Choice: {CYAN}").upper()

    #Takes user input and opens sub routines
        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            higher_lower()
        elif choice == "D":
            stats()
        elif choice == "X":
            save_stats()
            print(f"{YELLOW}Come again soon :D")
            time.sleep(0.25)
            exit_flag = True

def number_features():
    """Displays features of the number entered"""
    while True:
        #"""Displays features of a number"""
        clear_screen()
        global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER
        try:
            number = int(input(f"{GREEN}Please enter a whole number that can be checked over: {CYAN}"))
            if number == int:
                print(f"{YELLOW}The features of {number} are...")
        except ValueError:
            print(F"{YELLOW}Please input an integer")
            print(F"{YELLOW}Press enter to return to main menu")
            break

        #Check if the number is odd or even
        if number > 0:
            print(F" {YELLOW}Positive")
        elif number < 0:
            print(F" {YELLOW}Negative")
        else:
            print(F" {YELLOW}Zero")

        #Check if the number is odd or even
        if number % 2 == 0:
            print(F" {YELLOW}Even")
        else:
            print(F"{YELLOW} Odd")

        #Lists all the factors of the number
        print(F" Factors are{RED}", end="")
        factor_count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                print(" " + str(i), end="")
                factor_count += 1

        #Check if number is a prime
        if factor_count == 2:
            print(F"\n {YELLOW}Is a prime number")
        else:
            print(F"\n {YELLOW}Is not a prime number")
        
        #Displays number as Binary, Hexadecimal and Octal
        print(f" {YELLOW}Binary: {RED}{bin(number)}{YELLOW}")
        print(f" {YELLOW}Hexadecimal: {RED}{hex(number)}{YELLOW}")
        print(f" {YELLOW}Octal: {RED}{oct(number)}{YELLOW}")

        #Update global variables
        if NUMBER_COUNT == 0:
            SMALLEST_NUMBER == number
            LARGEST_NUMBER == number
        else:
            SMALLEST_NUMBER = min(number, SMALLEST_NUMBER)
            LARGEST_NUMBER = max(number, LARGEST_NUMBER)

        NUMBER_COUNT += 1
        NUMBER_TOTAL += number

        #Asks user if they want to check another number
        again = input(F"{GREEN}Do you want to check another number (y/n)?: {CYAN}").lower()
        if again != "y":
            print(F"{YELLOW}Press Enter to return to main menu")
            break
    input()


def draw_graph(table):
    """Draws the graph for the plotter routine"""
    print(F"{RED}                                                     x axis")
    print(F"{RED}     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38")
    print(F"{RED}  --------------------------------------------------------------------------------------------------------------------")
    for i, row in enumerate(table, start=1):
        print(f"{i:2}|  {'  '.join(row)} |")
    print(F"{RED}  --------------------------------------------------------------------------------------------------------------------")


def plotter():
    """Plot x and y cords on a table"""
    clear_screen()
    #Creates a blank table with specified rows and columns
    global PLOT_COUNT
    num_columns = 38
    num_rows = 12
    table = [[" " for column in range(num_columns)] for row in range(num_rows)]
    draw_graph(table)
    print(F"{GREEN}Enter a coordinate below to be added to the plot")
    while True:
        try:
            x_axis = int(input(F"{GREEN}x axis: {CYAN}"))
            if 0 < x_axis <= num_columns:
                y_axis = int(input(F"{GREEN}y axis: {CYAN}"))
                if 0 < y_axis <= num_columns:
                    clear_screen()
                    PLOT_COUNT += 1
                    table[y_axis - 1] [x_axis - 1] = F"{GREEN}x{RED}"
                    if 0 < x_axis <= num_rows:
                        draw_graph(table)
                        another_cord = input(F"{GREEN}Do you wish to add another coordinate (y/n)? {CYAN}").lower()
                        if another_cord != 'y':
                            break
                elif y_axis > 12:
                    break
            elif x_axis > 38:
                break
        except ValueError:
            print(F"{YELLOW}Invalid input. Please use integers.")

def higher_lower():
    """Higher-or-Lower game"""
    clear_screen()
    global TOTAL_GUESSES, CORRECT_GUESSES, TOTAL_INVALID_GUESSES
    print(F"{YELLOW}Hello and welcome to Higher or Lower!!!")
    time.sleep(0.5)
    print("A game where you have to guess the magic number between 1-10")
    time.sleep(0.5)
    print("But be wary, for if you shall exceed 5 attempts, you will be out!")
    time.sleep(0.5)
    print(F"Good luck player!!!{RESET}")
    time.sleep(0.5)

    num = random.randint(1, 10)
    try:
        count = 1
        while count < 6:
            guess = int(input(F"{GREEN}What do you think it is?: {CYAN}"))
            if guess == num:
                print(F"{YELLOW}BAZINGA! You are correct!")
                print(f"You guessed it in {RED}{count}{YELLOW} guesses")
                print(F"Press enter to return to main menu{RESET}")
                CORRECT_GUESSES += 1
                TOTAL_GUESSES += 1
                break
            elif guess == 67:
                print(f"{RED}89. {count}/5")
                time.sleep(0.67)
                TOTAL_GUESSES += 1
                count += 1
            elif guess > 10:
                print(F"{YELLOW}Please enter a number between 1-10!")
                time.sleep(0.5)
                TOTAL_INVALID_GUESSES += 1
            elif guess < 1:
                print(F"{YELLOW}Please enter a number between 1-10!")
                time.sleep(0.5)
                TOTAL_INVALID_GUESSES += 1
            elif guess > num:
                print(f"{YELLOW}WRONG! Lower. {RED}{count}/5{RESET}")
                TOTAL_GUESSES += 1
                count += 1
            elif guess < num:
                print(f"{YELLOW}WRONG! Higher. {RED}{count}/5{RESET}")
                TOTAL_GUESSES += 1
                count += 1
        else:
            print(F"{YELLOW}Oh No! You ran out of attempts.")
            print(f"{YELLOW}The number we were looking for was {RED}{num}")
            print(F"{YELLOW}Press enter to return to the main menu")
    except ValueError:
        print(F"{YELLOW}Invalid input! Please input an integer")
        TOTAL_INVALID_GUESSES += 1
        time.sleep(0.5)
        print(f"Press Enter to return to menu{RESET}")
    input()

def stats():
    """Show statistics about numbers used in app"""
    clear_screen()
    print("Here are your statistics of overall use:")
    print(f" Numbers entered:  {NUMBER_COUNT}")
    print(f" Total of numbers:  {NUMBER_TOTAL}")
    print(f" Average of Numbers:  {NUMBER_TOTAL / NUMBER_COUNT}")
    print(f" Smallest number entered:  {SMALLEST_NUMBER}")
    print(f" Largest Number entered:  {LARGEST_NUMBER}")
    print(f" Total Guesses: {TOTAL_GUESSES}")
    print(f" Total Invalid Guesses: {TOTAL_INVALID_GUESSES}")
    print(f" Total Correct Guesses: {CORRECT_GUESSES}")
    print(f" Higher-Lower Win Rate: {CORRECT_GUESSES / TOTAL_GUESSES:.2f}%")
    print("Press enter to return to main menu")
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
        f.write(f"{TOTAL_GUESSES}\n")
        f.write(f"{TOTAL_INVALID_GUESSES}\n")
        f.write(f"{CORRECT_GUESSES}\n")

def load_stats():
    """Loads statistics from previous session"""
    try:
        with open('stats.txt', 'r') as f:
            global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER, PLOT_COUNT, TOTAL_GUESSES, TOTAL_INVALID_GUESSES, CORRECT_GUESSES
            NUMBER_COUNT = int(f.readline())
            NUMBER_TOTAL = int(f.readline())
            SMALLEST_NUMBER = int(f.readline())
            LARGEST_NUMBER = int(f.readline())
            PLOT_COUNT = int(f.readline())
            TOTAL_GUESSES = int(f.readline())
            TOTAL_INVALID_GUESSES = int(f.readline())
            CORRECT_GUESSES = int(f.readline())
    except FileNotFoundError:
        NUMBER_COUNT = 0
        NUMBER_TOTAL = 0
        SMALLEST_NUMBER = 0
        LARGEST_NUMBER = 0
        PLOT_COUNT = 0
        TOTAL_GUESSES = 0
        TOTAL_INVALID_GUESSES = 0
        CORRECT_GUESSES = 0

main()