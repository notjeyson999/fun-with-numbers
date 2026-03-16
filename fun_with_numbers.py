"""Recreation of the original Fun with numbers program"""
#Developed by Jeyson Blain :P

#Imports required libraries
import os

def main():
    """The main menu"""
    #Sets exit condition to false
    exit_flag = False

    while not exit_flag:
        clear_screen()
        print('Welcome to Fun With Numbers')
        print('Choose from the menu below:')
        print(' (A) Check number features')
        print(' (B) Plot numbers')
        print(' (C) Check overall stats')
        print('\n (X) Save and exit')
        choice = input('Choice: ').upper()

    #Takes user input and opens sub-routines
        if choice == 'A':
            number_features()
            input()
        elif choice == 'B':
            plotter()
        elif choice == 'C':
            stats()
        elif choice == 'X':
            exit_flag = True
#
def number_features():
    """Displays features of a number"""
    clear_screen()
    #print("Number features routine")
    number = int(input("Please enter a whole number that can be checked over: "))
    print(f"\nThe features of {number} are...")
    if number > 0:
        print(" Positive")
    elif number < 0:
        print(" Negative")
    else:
        print(" Zero")

    #Check if number is odd or even
    if number % 2 == 0:
        print(" Even")
    else:
        print(" Odd")


    #List all factors of the number
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

def draw_graph():
    """Draws the graph for the plotter routine"""
    print("                                                       x axis")
    print("      1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38")
    print("   --------------------------------------------------------------------------------------------------------------------")
    print("   --------------------------------------------------------------------------------------------------------------------")

def plotter():
    """Plot x and y cords on a table"""
    clear_screen()
    print("Plotter routine")
    input()

def stats():
    """Show statistics about numbers used in app"""
    clear_screen()
    #Creates a blank table with specified rows and columns#
    num_columns = 38
    num_rows = 12
    table = [[" " for column in range(num_columns)] for row in range(num_rows)]
    print("Statistics routine")
    input()

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

main()
