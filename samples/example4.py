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
    
play = "y"
while play == "y":
		user_choice = input("Please choose rock, paper, or scissors: ")
		computer_choice = random.choice(["rock", "paper", "scissors"])
		print("The computer chose", computer_choice)
		if user_choice == computer_choice:
			print("It's a tie!")
		elif user_choice == "rock":
			if computer_choice == "paper":
				print("The computer wins!")
			else:
				print("You win!")
		elif user_choice == "paper":
			if computer_choice == "scissors":
				print("The computer wins!")
			else:
				print("You win!")
		elif user_choice == "scissors":
			if computer_choice == "rock":
				print("The computer wins!")
			else:
				print("You win!")
		else:
			print("That's not a valid choice!")
		play = input("Would you like to play again? (y/n): ")
print("Thanks for playing!")
    
main()