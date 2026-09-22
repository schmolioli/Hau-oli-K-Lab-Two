import random

game_number=random.randint(1,10)
guess_count = 0

while(True):
    guess=int(input("Guess a number between 1-10:"))
    guess_count += 1
    if guess>game_number:
        print("too high")
    elif guess<game_number:
        print("too low")
    else:
        print(f"correct! It took you {guess_count} guesses.")
        break