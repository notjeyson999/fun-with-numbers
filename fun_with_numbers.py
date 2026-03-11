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
    print(f"The features of {number} are...")
    if number > 0:
        print(" Positive")
    elif number < 0:
        print(" Negative")
    else:
        print(" Zero")
    input()

def plotter():
    """Plot x and y cords on a table"""
    clear_screen()
    print("Plotter routine")
    input()
def stats():
    """Show statistics about numbers used in app"""
    clear_screen()
    print("Statistics routine")
    input()

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

main()