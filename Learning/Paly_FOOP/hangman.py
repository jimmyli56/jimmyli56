import random

# List of words to choose 
words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
         "computer", "python", "program", "glasses", "sweatshirt",
         "sweatpants", "mattress", "friends", "clocks", "biology",
         "algebra", "suitcase", "knives", "ninjas", "shampoo"]

# Selects a random word from the list
word = random.choice(words)

# Creates a list of underscores the same length as the selected word
guesses = ["_"] * len(word)

# Set the number of remaining guesses to 6
remaining_guesses = 6

# Main game loop
while remaining_guesses > 0:
    # Prints the current state of the game
    print("Current word: ", " ".join(guesses))
    print("Remaining guesses: ", remaining_guesses)

    # Get the player's next guess
    guess = input("Guess a letter: ")

    # Checks if the guess is correct
    if guess in word:
        # If the guess is correct, update the list of guesses
        for i in range(len(word)):
            if word[i] == guess:
                guesses[i] = guess
    else:
        # If guess is incorrect, decrease the number of remaining guesses
        remaining_guesses -= 1

    # Check if the player has won
    if "_" not in guesses:
        print("Congratulations! You won!")
        break

# If the player has used all of their guesses and not won, they lose and the game stops.
if remaining_guesses == 0:
    print("Sorry, you lost. The correct word was: ", word)
