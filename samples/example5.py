#write a rock, paper, scissors game
#user inputs rock, paper, or scissors
#computer randomly chooses rock, paper, or scissors
#compare the two choices
#declare the winner
#ask if the user wants to play again
#keep track of the score
#declare the winner of the game

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("The first player to win 3 rounds wins the game.")
    print("Good luck!")
    print()
    user_score = 0
    computer_score = 0
    while user_score < 3 and computer_score < 3:
        user_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("The computer chose", computer_choice)
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Paper covers rock. You lose!")
                computer_score += 1
            else:
                print("Rock smashes scissors. You win!")
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Scissors cut paper. You lose!")
                computer_score += 1
            else:
                print("Paper covers rock. You win!")
                user_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Rock smashes scissors. You lose!")
                computer_score += 1
            else:
                print("Scissors cut paper. You win!")
                user_score += 1
        else:
            print("Invalid choice. Please try again.")
        print()
        print("The score is:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print()
    if user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")

main()

