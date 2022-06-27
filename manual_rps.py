import random


   
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer
    ##%    


def get_user_choice():
    player = input('rock, paper, or scissors?: ').lower()
    return player

def get_winner(computer,player):
    if computer == player:
        print("it'\s a tie")
    elif computer == "rock":
        if player == 'scissors':
            print("Computer won")
        if player == "paper":
            print("player won")
    elif computer == "paper":
        if player == 'rock':
            print("Computer won")
        if player == 'scissors':
            print("player won")
    elif computer == "scissors":
        if player == 'paper':
            print("Computer won")
        if player == 'rock':
            print("player won")
    
    else:
        print('big error')
    return 
        


def play():
    comp_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(user_choice, comp_choice)
    return

play()
    

    
 # #

 #def play_game()


 #play_again = input("Play again? (yes/no): ").lower()

 #if play_again != "yes":
     #break

