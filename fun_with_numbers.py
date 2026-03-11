"""Recreation of the original Fun with numbers program"""
#Developed by Jeyson Blain :P

def main():
    """The main menu"""
    exit_flag = False
    while not exit_flag:
        print('Welcome to Fun With Numbers')
        print('Choose from the menu below:')
        print(' (A) Check number features')
        print(' (B) Plot numbers')
        print(' (C) Check overall stats')
        print('\n (X) Save and exit')
        choice = input('Choice: ').upper()
    
        if choice == 'A':
            number_features()
            input()
            pass
        elif choice == 'B':
            pass
        elif choice == 'C':
            pass
        elif choice == 'X':
            exit_flag = True

def number_features():
    """Displays features of a number"""
    print("Number features routine")
    input()
def plotter():
    """Plot x and y cords on a table"""
    print("Plotter routine")
    input()
def stats():
    """Show statistics about numbers used in app"""
    print("Statistics routine")
    input()

main()