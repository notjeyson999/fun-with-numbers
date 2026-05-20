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
        f.write(f"\n{username},{password}\n")


logins = load_logins()


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
    print("\n=== Login ===")

    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in logins and logins[username] == password:
            print("Login successful\n")
            return

        print("Incorrect username or password.")


def main():
    print("Welcome to MAIN")
    print("123")


# Program start
while True:
    print("\n1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        login()
        main()
        break

    elif choice == "2":
        create_account()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid option.")
