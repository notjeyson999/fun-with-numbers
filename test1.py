import random

def unique_nummber_wordle():
    secret = "".join(random.sample("0123456789", 4))
    
    print("--- Unique Number Wordle ---")
    print("Guess the 4-digit number (no repeating digits!)")

    try:
        count = 1
        while count < 6:
            guess = input(f"Attempt {count}/5: ")
            if guess == secret:
                print("Good answer nephew")
            
            if len(guess) != 4 or not guess.isdigit():
                print("4 numbers only")
                continue
            if len(set(guess)) != 4:
                print("No duplicates allowed")
            
            result = []
            for idx in range(4):
                if guess[idx] == secret[idx]:
                    result.append("🟩")
                elif guess[idx] in secret:
                    result.append("🟨")
                else:
                    result.append("⬜️")
            print("Feedback: " + "".join(result))
            count += 1
        else:
            print("oh no!")
            return
    except ValueError:
        print("thats not a number")
unique_nummber_wordle()