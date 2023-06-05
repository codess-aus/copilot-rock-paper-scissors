# Write a rock, paper, scissors game
# import random module
import random

# define main function that handles all the logic


def main():
    # create a list of choices
    choices = ['rock', 'paper', 'scissors']
    # create a variable to hold the computer's choice
    computer_choice = random.choice(choices)
    # create a variable to hold the user's choice
    user_choice = input("Choose rock, paper, or scissors: ")
    # check if the user's choice is valid
    if user_choice in choices:
        # check if the user's choice is the same as the computer's choice
        if user_choice == computer_choice:
            # display a message saying it's a tie
            print("It's a tie!")
        # check if the user chose rock
        elif user_choice == 'rock':
            # check if the computer chose paper
            if computer_choice == 'paper':
                # display a message saying the computer wins
                print("Paper covers rock. The computer wins!")
            # otherwise
            else:
                # display a message saying the user wins
                print("Rock smashes scissors. You win!")
        # check if the user chose paper
        elif user_choice == 'paper':
            # check if the computer chose scissors
            if computer_choice == 'scissors':
                # display a message saying the computer wins
                print("Scissors cut paper. The computer wins!")
            # otherwise
            else:
                # display a message saying the user wins
                print("Paper covers rock. You win!")
        # check if the user chose scissors
        elif user_choice == 'scissors':
            # check if the computer chose rock
            if computer_choice == 'rock':
                # display a message saying the computer wins
                print("Rock smashes scissors. The computer wins!")
            # otherwise
            else:
                # display a message saying the user wins
                print("Scissors cut paper. You win!")
    # otherwise
    else:
        # display an error message saying the user's choice is invalid
        print("Error: Invalid choice.")

# call the main function
if __name__ == '__main__':
    main()


    