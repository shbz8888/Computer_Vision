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

get_computer_choice()
get_user_choice()


    

    
 # #

 #def play_game()


 #play_again = input("Play again? (yes/no): ").lower()

 #if play_again != "yes":
     #break

