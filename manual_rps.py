import random


# computer randomly selects a choice   
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer


# user is asked to input their choice  
def get_user_choice():
    player = input('rock, paper, or scissors?: ').lower()
    return player
 
# The winner is decided after the computer and player have made their decisions   
def get_winner(computer,player):
    if computer == player:
        print("it's a tie")
    elif computer == "rock" and player == 'scissors':
        print("Computer won")
    elif computer == "rock" and player == 'paper':
        print("Player won")
    elif computer == "paper" and player == 'scissors':
        print("Player won")
    elif computer == "paper" and player == 'rock':
        print("Computer won")
    elif computer == "scissors" and player == 'paper':
        print("Computer won")
    elif computer == "scissors" and player == 'rock':
        print("Player won")
    else:
        print('Try again')
    return 
 

# A play function to run the game
def play():
    computer = get_computer_choice()
    player = get_user_choice()
    winner = get_winner(computer,player)
    return
#  The play function is called
play()

