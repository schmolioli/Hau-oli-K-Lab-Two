import random

game_number=random.randint(1,10)

while(True):
    guess=int(input("Guess a number between 1-10:"))
    if guess>game_number:
        print("too high")
    elif guess<game_number:
        print("too low")
    else:
        print("correct!")
        break