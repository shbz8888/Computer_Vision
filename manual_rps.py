import random

def get_winner(computer,player):
    if computer == player:
        print('it\'s a tie')
    elif (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
        print('computer won')
    else:
        print('player won congratualtions')
    


def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer
 ##%    

def get_user_choice():
    player = input('rock, paper, or scissors?: ').lower()
    return player

get_computer_choice()
get_user_choice()



    

    
 # #

 #def play_game()


 #play_again = input("Play again? (yes/no): ").lower()

 #if play_again != "yes":
     #break

