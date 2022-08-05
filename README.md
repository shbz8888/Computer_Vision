# Computer_Vision
A program to play Rock Paper scissors with your computer

Milestone 1

* Using google's teachable machine a machine learing model was created that uses the camera to recognize when then user is holding up a rock, paper or scissors.
* In order to inicrease the accuracy of the model upto 500 images were uploaded to each category.
* google's teachable machine was chosen due to it being intuitive and easy to use

Milesone 2

* a new virtual environment was created using visual stdio code, this was done so that the computer could run the machine learning model
* after the model created in milestone 1 was downloaded and input into the right folder `python CVRPS.py` was entered into the terminal to run the model
* The model accessed the webcam and output a vector with 4 values each corresponding with the probability that the user is holding up either a rock, paper, scissors or nothing

The code used to run the mode:
```python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
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
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

Milestone 3

* In milestone 3 a manual version of the rock, paper, scissors game was created where the computer picked an option and then the user was asked to input an option before a winner was selected.

code for game:
```python
import random


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
    computer = get_computer_choice()
    player = get_user_choice()
    winner = get_winner(computer,player)
    return
#  The play function is called
play()
```
Milestone 4:
* The previous manual version of RPS was integrated into a new code where the camera was used to ascertain the user's choice, this was done using tensorflow and the model from google's teachable machine in a virtual environment
* The code from milestone 2 was created into a new function in order to turn on the camera and a countdown was added:
```python
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
```
* The countdown feature prints a countdown on the terminal before eventually telling the user to 'show your hand,' the user input is then taken 
* Once the countdown reaches 1 an array is printed which shows the probability of the user's sign being either a rock, paper, scissors or nothing
![](Images/Screenshot_1.png)    ![](Images/Screenshot_2.png)