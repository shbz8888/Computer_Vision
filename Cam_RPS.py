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
       
        #creates a countdown in terminal
        elapsed = time.time()-t_0
        
        if 7 <= 10 - elapsed <=8:
            print('get ready!')
        if 6 <= 10 -elapsed <=7:
            print('3!')
        if 5<= 10 -elapsed <=6:
            print('2!')
        if 4<= 10 -elapsed <=5:
            print('1!')
            print(prediction)
        if 10- elapsed <= 4:
            print('show your hand')
            print(prediction)
        if 10 - elapsed <=2:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
   
    cap.release()
   
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
    print(f'your choice is {player}' )
    return player
 

def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer

def get_user_choice():
    player = input('rock, paper, or scissors?: ').lower()
    return player
 

def get_winner(computer,player):
    if computer == player:
        print("it's a tie")
        return 'tie'
    elif computer == "rock" and player == 'scissors':
        print("Computer won")
        return 'Wcomputer'
    elif computer == "rock" and player == 'paper':
        print("Player won")
        return 'Wplayer'
    elif computer == "paper" and player == 'scissors':
        print("Player won")
        return 'Wplayer'
    elif computer == "paper" and player == 'rock':
        print("Computer won")
        return 'Wcomputer'
    elif computer == "scissors" and player == 'paper':
        print("Computer won")
        return 'Wcomputer'
    elif computer == "scissors" and player == 'rock':
        print("Player won")
        return 'Wplayer'
    else:
        print('Try again')
    return 
 


def play():
    prediction = turn_on_cam()
    player = Find_user_choice(prediction)
    computer = get_computer_choice()
    winner = get_winner(computer,player)



def play_best_of():
    player_wins = 0
    computer_wins = 0
    ties = 0
    rounds = 0
    while rounds < 4:
        winner = play()
        if winner == 'Wplayer':
            player_wins += 1
            print(f'player score is : {player_wins}')
        elif winner == 'Wcomputer':
            computer_wins += 1
            print(f'computer score is : {computer_wins}')
        rounds += 1
    if player_wins == computer_wins:
        print('The game is a draw')
    elif player_wins > computer_wins:
        print('Congrats ')
    else:
        print('You lost')
    return


play_best_of()