# rock paper scissors lizard spock by Jimmy Li 
import random
def name_to_number(name):
# converts name of action to a number, using if/elif/else statements
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: Invalid name"

def number_to_name(number):
# converts number to a name of action, using if/elif/else statements
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: Invalid number"

def rpsls(player_choice):
    # Plays the game using the functions above
    print()
    print("Player chooses", player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice)
    difference = (player_number - comp_number) % 5
    if difference == 0:
        print("Player and computer tie!")
    elif difference <= 2:
        print("Player wins!")
    else:
        print("Computer wins!")

rpsls(input("rock, paper, sissor, lizard, spock. what is your choice?\n"))