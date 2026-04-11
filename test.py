from colorama import init, Fore, Style

init(autoreset=True)

colors = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA
]

text = input("Enter text: ")

for i, char in enumerate(text):
    if char.isalpha():
        print(colors[i % len(colors)] + char, end="")
    else:
        print(char, end="")

print()