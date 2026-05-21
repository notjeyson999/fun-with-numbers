'''Recreation of the original Fun with Numbers''' 
#Devoloped by Jeyson Blain :P

#Imports required libraries
import os
#Imports time function
import time
#Imports random for higher or lower feature
import random
#Imports
import sys

#States Colours for UI
RESET   = '\033[0m'  #Sets to default#
RED     = '\033[31m' #Special Characters/Numbers#
GREEN   = '\033[32m' #Choices#
YELLOW  = '\033[33m' #Text#
CYAN    = '\033[36m' #Input Text#
BLUE    = '\033[94m' #Headings#
MAGENTA = '\033[35m' #Input Requirement#
GREY    = '\033[90m' #Number Wordle Absence#

#State global variables
NUMBER_COUNT = 0
NUMBER_TOTAL = 0
SMALLEST_NUMBER = 0
LARGEST_NUMBER = 0
PLOT_COUNT = 0
TOTAL_GUESSES = 0
TOTAL_INVALID_GUESSES = 0
CORRECT_GUESSES = 0
startup_shown = False
loading_shown = False

def startup_screen():
    """Start-up screen"""
    global startup_shown

    clear_screen()

    if startup_shown:
        return
    
    startup_shown = True

    clear_screen()
    print(f"{GREEN}*" * 26)
    print("*                        *")
    print("*    FUN WITH NUMBERS    *")
    print("*       LOADING...       *")
    print("*                        *")
    print("*" * 26)
    time.sleep(2)
    clear_screen()
    print(f"{GREEN}*" * 26)
    print("*                        *")
    print("*     WELCOME BACK!      *")
    print("*                        *")
    print("*" * 26)
    time.sleep(0.5)
    clear_screen()

def load_logins():
    users = {}
    try:
        with open("user_access.txt", "r", encoding="utf8") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username.strip()] = password.strip()
    except FileNotFoundError:
        pass  # No file yet, no users yet
    return users


def save_login(username, password):
    with open("user_access.txt", "a", encoding="utf8") as f:
        f.write(f"\n{username},{password}")


logins = load_logins()
LOGGED_IN = False


def create_account():
    print("\n=== Create New Account ===")

    while True:
        username = input("Choose a username: ").strip()

        if username in logins:
            print("That username already exists. Try another.")
            continue

        password = input("Choose a password: ").strip()
        confirm = input("Confirm password: ").strip()

        if password != confirm:
            print("Passwords do not match. Try again.")
            continue

        save_login(username, password)
        logins[username] = password
        print("Account created successfully.\n")
        return

def login():
    global LOGGED_IN
    print("\n=== Login ===")

    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in logins and logins[username] == password:
            print("Login successful\n")
            LOGGED_IN = True
            main()
            return

        print("Incorrect username or password.")


def main():
    '''The main menu'''
    #Sets the exit condition to false
    load_stats()
    exit_flag = False

    while not exit_flag:
        startup_screen()
        load_logins()
        print(f"{GREEN}==============================")
        print(f"{GREEN}Welcome to Fun with Numbers!")
        print(f"{GREEN}Choose from the menu below:{RESET}")
        print(f" {GREEN}(A){RESET} {YELLOW}Check number features")
        print(f" {GREEN}(B){RESET} {YELLOW}Plot numbers")
        print(f" {GREEN}(C){RESET} {YELLOW}Higher or Lower")
        print(f" {GREEN}(D){RESET} {YELLOW}Number Wordle")
        print(f" {GREEN}(E){RESET} {YELLOW}Check overall stats")
        print(f"\n {GREEN}(X){RESET} {YELLOW}Save and exit")
        print(f"{GREEN}==============================")
        choice = input(f"{MAGENTA}Choice: {CYAN}").upper()

    #Takes user input and opens sub routines
        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            higher_lower()
        elif choice == "D":
            number_wordle()
        elif choice == "E":
            stats()
        elif choice == "X":
            save_stats()
            print(f"{YELLOW}Saving stats", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\rStats Saved!")
            print(f"{GREEN}Come again soon :D")
            time.sleep(0.25)
            exit_flag = True

def number_features():
    """Displays features of the number entered"""
    while True:
        #"""Displays features of a number"""
        clear_screen()
        global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER
        try:
            number = int(input(f"{MAGENTA}Please enter a whole number that can be checked over: {CYAN}"))
            if number == int:
                print(f"{YELLOW}The features of {RED}{number} are...")
        except ValueError:
            print(F"{RED}Please input an integer")
            print(F"{YELLOW}Press enter to return to main menu")
            break

        #Check if the number is odd or even
        if number > 0:
            print(F" {GREEN}Positive")
        elif number < 0:
            print(F" {RED}Negative")
        else:
            print(F" {GREY}Zero")

        #Check if the number is odd or even
        if number % 2 == 0:
            print(F" {GREEN}Even")
        else:
            print(F"{RED} Odd")

        #Lists all the factors of the number
        print(F" {YELLOW}Factors are{RED}", end="")
        factor_count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                print(" " + str(i), end="")
                factor_count += 1

        #Check if number is a prime
        if factor_count == 2:
            print(F"\n {GREEN}Is a prime number")
        else:
            print(F"\n {RED}Is not a prime number")
        
        #Displays number as Binary, Hexadecimal and Octal
        binary = f"{bin(number)}"
        binary1 = binary[2:]
        hexadecimal = f"{hex(number)}"
        hexadecimal1 = hexadecimal[2:]
        octal = f"{oct(number)}"
        octal1 = octal[2:]
        print(f" {YELLOW}Binary: {RED}{binary1}")
        print(f" {YELLOW}Hexadecimal: {RED}{hexadecimal1}")
        print(f" {YELLOW}Octal: {RED}{octal1}")

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
        again = input(F"{MAGENTA}Do you want to check another number (y/n)?: {CYAN}").lower()
        if again != "y":
            print(F"{MAGENTA}Press Enter to return to main menu")
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
    print(F"{YELLOW}Enter a coordinate below to be added to the plot")
    while True:
        try:
            x_axis = int(input(F"{MAGENTA}x axis: {CYAN}"))
            if 0 < x_axis <= num_columns:
                y_axis = int(input(F"{MAGENTA}y axis: {CYAN}"))
                if 0 < y_axis <= num_columns:
                    clear_screen()
                    PLOT_COUNT += 1
                    table[y_axis - 1] [x_axis - 1] = F"{GREEN}x{RED}"
                    if 0 < x_axis <= num_rows:
                        draw_graph(table)
                        another_cord = input(F"{MAGENTA}Do you wish to add another coordinate (y/n)? {CYAN}").lower()
                        if another_cord != 'y':
                            break
                elif y_axis >= 12:
                    print(f"{RED}no")
            elif x_axis >= 38:
                print(f"{RED}Please enter an integer between 1-38!")
        except ValueError:
            print(F"{RED}Invalid input. Please use integers.")

def higher_lower():
    """Higher-or-Lower game"""
    clear_screen()
    global TOTAL_GUESSES, CORRECT_GUESSES, TOTAL_INVALID_GUESSES
    print(f"{YELLOW}Welcome to Higher-or-Lower")
    print(f"{BLUE}How To Play:")
    print(f"{YELLOW}Guess the secret number between {RED}1-10")
    print(f"ZERO{YELLOW} is {RED}NOT{YELLOW} allowed")
    print(f"{YELLOW}If your guess is more than the secret number, than it will tell you to guess lower")
    print("If your guess is less than the secret number, than it will tell you to guess higher")
    print(f"You have {RED}5{YELLOW} guesses")
    print(f"{RED}Invalid inputs will send you back to the menu")

    num = random.randint(1, 10)
    try:
        count = 1
        while count < 6:
            guess = int(input(F"{MAGENTA}What do you think it is?: {CYAN}"))
            if guess == num:
                print(F"{GREEN}BAZINGA!{YELLOW} You are correct!")
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
                print(F"{RED}Please enter a number between 1-10!")
                time.sleep(0.5)
                TOTAL_INVALID_GUESSES += 1
            elif guess < 1:
                print(F"{RED}Please enter a number between 1-10!")
                time.sleep(0.5)
                TOTAL_INVALID_GUESSES += 1
            elif guess > num:
                print(f"{RED}WRONG!{YELLOW} Lower. {RED}{count}/5{RESET}")
                TOTAL_GUESSES += 1
                count += 1
            elif guess < num:
                print(f"{RED}WRONG!{YELLOW} Higher. {RED}{count}/5{RESET}")
                TOTAL_GUESSES += 1
                count += 1
        else:
            print(F"{YELLOW}Oh No! You ran out of attempts.")
            print(f"{YELLOW}The number we were looking for was {RED}{num}")
            print(F"{YELLOW}Press enter to return to the main menu")
    except ValueError:
        print(F"{RED}Invalid input! Please input an integer")
        TOTAL_INVALID_GUESSES += 1
        time.sleep(0.5)
        print(f"{MAGENTA}Press Enter to return to menu{RESET}")
    input()

def get_feedback(secret, guess):
    """Provides Wordle-style feedback for number guesses."""
    result = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            result.append(f"\033[92m{guess[i]}\033[0m")  # Green: Correct spot
        elif guess[i] in secret:
            result.append(f"\033[93m{guess[i]}\033[0m")  # Yellow: Wrong spot
        else:
            result.append(f"\033[90m{guess[i]}\033[0m")  # Grey: Absent
    return " ".join(result)

def number_wordle():
    """Number Wordle game"""
    clear_screen()
    # Selects 4 unique digits from 0-9 and joins them as a string
    secret = "".join(random.sample("0123456789", 4))
    att = 5
    print(f"{YELLOW}Welcome to Number Wordle!")
    print(f"{BLUE}Rules:")
    print(f"{YELLOW}You have {RED}5 {YELLOW}attempts to guess the secret number")
    print(f"The secret number does {RED}NOT{YELLOW} contain any duplicates")
    print(f"There are {RED}4{YELLOW} numbers")
    print(f"{BLUE}Key:")
    print(f"{GREEN}Number is in the correct spot")
    print(f"{YELLOW}Number is in the secret but in the incorrect spot")
    print(f"{GREY}Number is not in the secret")
    
    for attempt in range(1, att + 1):
        attempt = input(f"{MAGENTA}Attempt {attempt}/5: {CYAN}")
        att += 1
        
        # Validates that input is exactly 4 digits
        if len(attempt) != 4 or not attempt.isdigit():
            print(f"{RED}Invalid input. Please enter a 4-digit number.")
            continue
            
        print(get_feedback(secret, attempt))
        
        if attempt == secret:
            print(f"{GREEN}Correct!{YELLOW} You guessed it in {RED}{att - 5}{YELLOW} attempts.")
            print("Press Enter to return to main menu")
            break
    else:
        print(f"{RED}Game Over!{YELLOW} The number was: {RED}{secret}{YELLOW}")
        print(f"{MAGENTA}Press Enter to return to main menu")
        

    input()

def stats():
    """Show statistics about numbers used in app"""
    clear_screen()
    print(f"{GREEN}Here are your statistics of overall use:")
    print(f" {YELLOW}Numbers entered:  {RED}{NUMBER_COUNT}")
    print(f" {YELLOW}Total of numbers:  {RED}{NUMBER_TOTAL}")
    print(f" {YELLOW}Average of Numbers:  {RED}{NUMBER_TOTAL / NUMBER_COUNT}")
    print(f" {YELLOW}Smallest number entered:  {RED}{SMALLEST_NUMBER}")
    print(f" {YELLOW}Largest Number entered:  {RED}{LARGEST_NUMBER}")
    print(f" {YELLOW}Total Guesses: {RED}{TOTAL_GUESSES}")
    print(f" {YELLOW}Total Invalid Guesses: {RED}{TOTAL_INVALID_GUESSES}")
    print(f" {YELLOW}Total Correct Guesses: {RED}{CORRECT_GUESSES}")
    print(f" {YELLOW}Higher-Lower Win Rate: {RED}{CORRECT_GUESSES / TOTAL_GUESSES:.2f}%")
    print(F"{MAGENTA}Press enter to return to main menu")
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

while True:
    clear_screen()
    print("\n1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        clear_screen()
        login()
        if LOGGED_IN:
            main()
            break

    elif choice == "2":
        clear_screen()
        create_account()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid option.")
