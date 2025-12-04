#!/usr/bin/env python3
"""
Number Guessing Game
Simple console game where the player guesses a randomly chosen number
Author: <Your Name>
"""

import random

def get_valid_int(prompt, min_val, max_val):
    """Prompt until user enters a valid integer between min_val and max_val."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"Please enter an integer between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def play_round(min_n=1, max_n=100, max_attempts=None):
    """Play one round. Returns True if player guessed correctly, else False."""
    secret = random.randint(min_n, max_n)
    attempts = 0
    if max_attempts is None:
        max_attempts = 10  # default cap if not provided

    print(f"\nI've picked a number between {min_n} and {max_n}. Can you guess it?")
    print(f"You have up to {max_attempts} attempts.\n")

    while attempts < max_attempts:
        guess = get_valid_int(f"Attempt {attempts+1}/{max_attempts} — Your guess: ", min_n, max_n)
        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed the number in {attempts} attempt(s).")
            return True, attempts
        elif guess < secret:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    print(f"\n❌ You've used all {max_attempts} attempts. The number was {secret}. Better luck next time!")
    return False, attempts

def main():
    print("=== Number Guessing Game ===")
    print("1) Play default game (1 to 100, 10 attempts)")
    print("2) Custom game settings")
    choice = get_valid_int("Choose an option (1 or 2): ", 1, 2)

    if choice == 1:
        min_n, max_n, max_attempts = 1, 100, 10
    else:
        min_n = get_valid_int("Enter minimum number (>= 0): ", 0, 10**9)
        max_n = get_valid_int(f"Enter maximum number (greater than {min_n}): ", min_n+1, 10**9)
        max_attempts = get_valid_int("Enter maximum attempts (1 - 1000): ", 1, 1000)

    wins = 0
    rounds_played = 0
    while True:
        rounds_played += 1
        won, used = play_round(min_n, max_n, max_attempts)
        if won:
            wins += 1
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

    print("\n=== Game Summary ===")
    print(f"Rounds played: {rounds_played}")
    print(f"Rounds won: {wins}")
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    main()
