#write a rock, paper, scissors game
# import random module
import random
# define main function that handles all the logic
def main():
    print('Welcome to Rock, Paper, Scissors!')
    print('Enter 1 for Rock, 2 for Paper, or 3 for Scissors')
  
  #looping until user creates a valid input
    while True:
        try:
            user_choice = int(input('Enter your choice: '))
            if user_choice not in [1,2,3]:
                print('Invalid choice. Please try again.')
            else:
                break
        except ValueError:
            print('Invalid choice. Please try again.')

    # initialize value of choice_name variable
    # corresponding to the choice value
    if user_choice == 1:
        choice_name = 'Rock'
    elif user_choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print user choice
    print('User choice is', choice_name)
    print('Now it\'s the computer\'s turn....')

    # Computer chooses randomly any number
    # among 1, 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice ==2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print('Computer choice is', comp_choice_name)

    # Compare the user and computer choices
    if user_choice == comp_choice:
        print('It\'s a tie!')
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        print('Computer wins! ' + comp_choice_name + ' beats ' + choice_name)
    else:
        print('You win! ' + choice_name + ' beats ' + comp_choice_name)

if __name__ == '__main__':
    main()

    




