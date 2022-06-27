import random
def get_winner(computer,player):
    if computer == player:
        print("it'\s a tie")
    elif computer == 'rock':
        if player == 'scissors':
            return print("Computer won")
        else:
            return print("Player won")
    elif computer == 'paper':
        if player == 'rock':
            return  print("Computer won")
        else:
            return print("Player won")
    elif computer == 'scissors':
        if player == 'paper':
            return  print("Computer won")
        else:
            return print("Player won")
    else:
        print('could not be processed')
    return 
   
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
get_winner(get_computer_choice(),get_user_choice())


    

    
 # #

 #def play_game()


 #play_again = input("Play again? (yes/no): ").lower()

 #if play_again != "yes":
     #break

