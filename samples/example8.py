# Create a Rock, Paper, Scissors Game where the user plays against the computer

import random

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")
print("The first to 3 points wins!")

player_score = 0
computer_score = 0

while True:
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("What would you like to play?")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    player_choice = int(input("Enter your choice: "))

    if player_choice == 1:
        print("You chose Rock!")
    elif player_choice == 2:
        print("You chose Paper!")
    elif player_choice == 3:
        print("You chose Scissors!")
    elif player_choice == 4:
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice!")

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print("The computer chose Rock!")
    elif computer_choice == 2:
        print("The computer chose Paper!")
    elif computer_choice == 3:
        print("The computer chose Scissors!")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 1 and computer_choice == 2:
        print("Paper beats Rock!")
        computer_score += 1
    elif player_choice == 1 and computer_choice == 3:
        print("Rock beats Scissors!")
        player_score += 1
    elif player_choice == 2 and computer_choice == 1:
        print("Paper beats Rock!")
        player_score += 1
    elif player_choice == 2 and computer_choice == 3:
        print("Scissors beats Paper!")
        computer_score += 1
    elif player_choice == 3 and computer_choice == 1:
        print("Rock beats Scissors!")
        computer_score += 1
    elif player_choice == 3 and computer_choice == 2:
        print("Scissors beats Paper!")
        player_score += 1

    if player_score == 3:
        print("You win!")
        break
    elif computer_score == 3:
        print("The computer wins!")
        break

print("Thanks for playing!")

# Path: copilot-rock-paper-scissors-demo\main.py