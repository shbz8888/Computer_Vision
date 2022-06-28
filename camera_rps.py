import random
import cv2
from keras.models import load_model
import numpy as np

# computer randomly selects a choice   
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f'computer choice is {computer}')
    return computer


# user is asked to input a choice  
def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
                
    # After the loop release the cap object
        cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
    if prediction[0] > 0.6:
        player = 'rock'
    elif prediction[1] > 0.6:
        player = 'paper'
    elif prediction[2] > 0.6:
        player = 'scissors'
    else: player = 'nothing'
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
    player = get_prediction()
    winner = get_winner(computer,player)
    return
#  The play function is called
play()

