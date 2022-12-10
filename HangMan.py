#HangMan

import random

# List of words to use in the game
WORDS = ["apple", "banana", "orange", "grape"]

# Select a random word from the list
word = random.choice(WORDS)

# Set up the game state
guesses = []  # List of letters the player has guessed
misses = 0   # Number of incorrect guesses

# Main game loop
while True:
    # Print the current state of the game
    print("Word: ", end="")
    for letter in word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("  Misses: ", misses)

    # Prompt the player for a letter to guess
    guess = input("Guess a letter: ").lower()

    # Check if the player has already guessed this letter
    if guess in guesses:
        print("You have already guessed this letter. Please try again.")
        continue

    # Check if the player's guess is correct
    if guess in word:
        print("Correct! Well done.")
        guesses.append(guess)
    else:
        print("Incorrect. Sorry.")
        misses += 1

    # Check if the player has won or lost
    if misses == 6:
        print("You have lost the game. The correct word was:", word)
        break
    if all(letter in guesses for letter in word):
        print("You have won the game! Congratulations.")
        break
