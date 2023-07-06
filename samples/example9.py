#write a rock, paper, scissors, lizard, spock game
#user inputs rock, paper, scissors, Lizard or spock
#computer randomly chooses rock, paper, scissors, lizard or spock
#compare the two choices
#declare the winner
#output the reason why the winner won
#keep track of the score, the game is won when best of 3 is reached
#declare the winner of the game
#ask if the user wants to play again
import random

def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    while rounds_played < 3:
        print("Round", rounds_played + 1)
        user_choice = input("Choose rock, paper, scissors, lizard, or spock: ")
        computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
        print("Computer chose", computer_choice)
        
        if user_choice == computer_choice:
            print("Tie!")
        elif (user_choice == "rock" and (computer_choice == "scissors")):
            print("You win! Rock smashes scissors")
            user_score += 1
        elif (user_choice == "rock" and (computer_choice == "lizard")):
            print("You win! Rock crushes lizard")
            user_score += 1
        elif (user_choice == "rock" and (computer_choice == "paper")):
            print("You lose! Paper covers rock")
            computer_score += 1
        elif (user_choice == "rock" and (computer_choice == "spock")):
            print("You lose! Spock vaporizes rock")
            computer_score += 1
        elif (user_choice == "paper" and (computer_choice == "rock")):
            print("You win! Paper covers rock")
            user_score += 1
        elif (user_choice == "paper" and (computer_choice == "spock")):
            print("You win! Paper disproves spock")
            user_score += 1
        elif (user_choice == "paper" and (computer_choice == "scissors")):
            print("You lose! Scissors cuts paper")
            computer_score += 1
        elif (user_choice == "paper" and (computer_choice == "lizard")):
            print("You lose! Lizard eats paper")
            computer_score += 1
        elif (user_choice == "scissors" and (computer_choice == "paper")):
            print("You win! Scissors cuts paper")
            user_score += 1
        elif (user_choice == "scissors" and (computer_choice == "lizard")):
            print("You win! Scissors decapitates lizard")
            user_score += 1
        elif (user_choice == "scissors" and (computer_choice == "rock")):
            print("You lose! Rock smashes scissors")
            computer_score += 1
        elif (user_choice == "scissors" and (computer_choice == "spock")):
            print("You lose! Spock smashes scissors")
            computer_score += 1
        elif (user_choice == "lizard" and (computer_choice == "paper")):
            print("You win! Lizard eats paper")
            user_score += 1
        elif (user_choice == "lizard" and (computer_choice == "spock")):
            print("You win! Lizard poisons spock")
            user_score += 1
        elif (user_choice == "lizard" and (computer_choice == "rock")):
            print("You lose! Rock crushes lizard")
            computer_score += 1
        elif (user_choice == "lizard" and (computer_choice == "scissors")):
            print("You lose! Scissors decapitates lizard")
            computer_score += 1
        elif (user_choice == "spock" and (computer_choice == "rock")):
            print("You win! Spock vaporizes rock")
            user_score += 1
        elif (user_choice == "spock" and (computer_choice == "scissors")):
            print("You win! Spock smashes scissors")
            user_score += 1
        elif (user_choice == "spock" and (computer_choice == "paper")):
            print("You lose! Paper disproves spock")
            computer_score += 1
        elif (user_choice == "spock" and (computer_choice == "lizard")):
            print("You lose! Lizard poisons spock")
            computer_score += 1
        else:
            print("Invalid choice! Learn to spell n00b!")

        print("Your score:", user_score)
        print("Computer score:", computer_score)
                
        rounds_played += 1
    
    if user_score > computer_score:
        print("You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game!")
    else:
        print("The game is tied!")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play_game()

play_game()