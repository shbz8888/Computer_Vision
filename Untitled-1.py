import random
import cv2
from keras.models import load_model
import numpy as np
import time 

def turn_on_cam():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    t_0 = time.time()
    while True: 

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        elapsed = time.time()-t_0

        print(10 - elapsed)
        print(prediction)
        if 7 <= 10 - elapsed <=8:
            print('get ready!')
        if 6 <= 10 -elapsed <=7:
            print('3!')
        if 5<= 10 -elapsed <=6:
            print('2!')
        if 4<= 10 -elapsed <=5:
            print('1!')
        if 10- elapsed <= 4:
            print('show your hand')
        if 10 - elapsed <=2:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction 

def Find_user_choice(prediction):
    if (prediction[0][0] > 6e-01) and (prediction[0][1] < 6e-01) and (prediction[0][2] < 6e-01) and (prediction[0][3] < 6e-01):
        player = 'rock'
    elif (prediction[0][1] > 6e-01) and (prediction[0][0] < 6e-01) and (prediction[0][2] < 6e-01) and (prediction[0][3] < 6e-01):
        player = 'paper'
    elif (prediction[0][2] > 6e-01) and (prediction[0][0] < 6e-01) and (prediction[0][1] < 6e-01) and (prediction[0][3] < 6e-01):
        player = 'scissors'
    else: player = 'nothing'
    return player
 

# computer randomly selects a choice   
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer


# user is asked to input a choice  
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
    prediction = turn_on_cam()
    computer = get_computer_choice()
    player = Find_user_choice(prediction)
    winner = get_winner(computer,player)
    return 
#  The play function is called

def play_best_of(winner):
    player_wins = 0
    computer_wins = 0
    ties = 0
    while player_wins < 4 and computer_wins <4:
        play()
        if winner == 'Player won':
            player_wins += 1
        elif winner == 'Computer won':
            computer_wins += 1
        elif winner == "its a tie":
            ties += 1
        elif player_wins == 3:
            print('Wow you won three rounds already')
            break 
        elif computer_wins == 3:
            print('Wow computer three rounds, better luck next time dude')
            break
        else:
            print('oh no')
        break

prediction = turn_on_cam()
computer = get_computer_choice()
player = Find_user_choice(prediction)
winner = get_winner(computer,player)
play_best_of(winner)


