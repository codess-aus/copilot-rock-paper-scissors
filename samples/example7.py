# Create a Rock, Paper, Scissors Game where the user plays against the computer
# The computer will randomly choose between rock, paper, or scissors
# The user will be prompted to choose between rock, paper, or scissors
# The winner will be determined by the following rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If both the computer and the user choose the same option, it's a tie
# The game will be best of 3 rounds
# The game will keep track of the score
# The game will end when either the user or the computer wins 2 rounds
# The game will ask the user if they want to play again
# If the user says yes, the game will start over
# If the user says no, the game will end
# The game will print the final score when the game ends

# Import the random module
import random

# Create a list of options for the computer to choose from
options = ["rock", "paper", "scissors"]

# Create a variable to keep track of the score
score = [0, 0]

# Create a variable to keep track of the number of rounds
rounds = 0

# Create a variable to keep track of whether the game is over
game_over = False

# Create a function to determine the winner of each round
def determine_winner(user_choice, computer_choice):
    # Print the user's choice
    print(f"You chose {user_choice}")

    # Print the computer's choice
    print(f"The computer chose {computer_choice}")

    # If the user and the computer chose the same option, it's a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    # If the user chose rock and the computer chose scissors, the user wins
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        score[0] += 1
    # If the user chose scissors and the computer chose paper, the user wins
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        score[0] += 1
    # If the user chose paper and the computer chose rock, the user wins
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        score[0] += 1
    # If the computer chose rock and the user chose scissors, the computer wins
    elif computer_choice == "rock" and user_choice == "scissors":
        print("The computer wins!")
        score[1] += 1
    # If the computer chose scissors and the user chose paper, the computer wins
    elif computer_choice == "scissors" and user_choice == "paper":
        print("The computer wins!")
        score[1] += 1
    # If the computer chose paper and the user chose rock, the computer wins
    elif computer_choice == "paper" and user_choice == "rock":
        print("The computer wins!")
        score[1] += 1

# Create a function to determine the winner of the game
def determine_game_winner():
    # If the user won 2 rounds, the user wins the game
    if score[0] == 2:
        print("You won the game!")
    # If the computer won 2 rounds, the computer wins the game
    elif score[1] == 2:
        print("The computer won the game!")

# Create a function to play the game
def play_game():
    # Create a variable to keep track of whether the game is over
    game_over = False

    # Create a while loop to play the game
    while game_over == False:
        # Create a variable to keep track of the number of rounds
        rounds = 0

        # Create a while loop to play each round
        while rounds < 3:
            # Prompt the user to choose rock, paper, or scissors
            user_choice = input("Choose rock, paper, or scissors: ")

            # Randomly choose rock, paper, or scissors for the computer
            computer_choice = random.choice(options)

            # Determine the winner of the round
            determine_winner(user_choice, computer_choice)

            # Increment the number of rounds
            rounds += 1

        # Determine the winner of the game
        determine_game_winner()

        # Prompt the user to play again
        play_again = input("Do you want to play again? (y/n) ")

        # If the user says yes, the game will start over
        if play_again == "y":
            print("Starting a new game...")
        # If the user says no, the game will end
        elif play_again == "n":
            print("Thanks for playing!")
            game_over = True

# Play the game
play_game()

# Print the final score
print(f"The final score is {score[0]} to {score[1]}")

# End of Rock, Paper, Scissors Game