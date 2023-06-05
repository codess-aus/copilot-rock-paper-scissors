import random

def main():
    print('Welcome to Rock, Paper, Scissors!')
    print('Enter 1 for Rock, 2 for Paper, or 3 for Scissors')

    # looping until user enter valid input
    while True:
        choice = int(input('Enter your choice: '))
        if choice in [1, 2, 3]:
            break
        else:
            print('Invalid input. Please enter 1, 2, or 3.')

    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
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
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print('Computer choice is', comp_choice_name)

    # Compare the user and computer choices
    if choice == comp_choice:
        print('It\'s a tie!')
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print('Computer wins! ' + comp_choice_name + ' beats ' + choice_name)
    else:
        print('You win! ' + choice_name + ' beats ' + comp_choice_name)

if __name__ == '__main__':
    main()