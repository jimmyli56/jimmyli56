import random

# List of words to choose for the game
words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
         "computer", "python", "program", "glasses", "sweatshirt",
         "sweatpants", "mattress", "friends", "clocks", "biology",
         "algebra", "suitcase", "knives", "ninjas", "shampoo"]

# Main game loop
while True:
    # Select a random word from the list
    word = random.choice(words)

    # Create a list of underscores the same length as the selected word, used to keep track of the player's guesses
    guesses = ["_"] * len(word)

    # Set the number of remaining guesses to 6
    remaining_guesses = 6

    # Main game loop
    while remaining_guesses > 0:
        # Print the current state of the game
        print("Current word: ", " ".join(guesses))
        print("Remaining guesses: ", remaining_guesses)

        # Get the player's next guess
        guess = input("Guess a letter: ")

        # Check if the guess is correct
        if guess in word:
            # If the guess is correct, update the list of guesses
            for i in range(len(word)):
                if word[i] == guess:
                    guesses[i] = guess
        else:
            # If the guess is incorrect, decrease the number of remaining guesses
            remaining_guesses -= 1

        # Check if the player has won
        if "_" not in guesses:
            print("Congratulations! You won!")
            break

    # If the player has used all of their guesses and did not won, they lose the game
    if remaining_guesses == 0:
        print("Sorry, you lost. The correct word was: ", word)

    # Prompt the player to play again
    again = input("Do you want to play again (y/n)? ")
    if again != "y":
      print("Thanks for playing!")
      break
