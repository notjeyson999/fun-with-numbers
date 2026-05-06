import random

def unique_number_wordle():
    # 1. Generate 4 unique digits
    secret = "".join(random.sample("0123456789", 4))
    attempts = 6
    
    print("--- Unique Number Wordle ---")
    print("Guess the 4-digit number (no repeating digits!)")

    for i in range(attempts):
        guess = input(f"\nAttempt {i+1}: ").strip()
        
        # Validation: 4 digits, all numbers, and unique
        if len(guess) != 4 or not guess.isdigit():
            print("❌ Enter exactly 4 digits.")
            continue
        if len(set(guess)) != 4:
            print("⚠️ Note: Your guess has duplicates, but the secret doesn't!")

        if guess == secret:
            print(f"🎉 Winner! The number was {secret}.")
            return

        # 2. Comparison logic
        result = []
        for idx in range(4):
            if guess[idx] == secret[idx]:
                result.append("🟩")
            elif guess[idx] in secret:
                result.append("🟨")
            else:
                result.append("⬜")
        
        print("Feedback: " + "".join(result))

    print(f"\nGame Over! The secret was {secret}.")

unique_number_wordle()
