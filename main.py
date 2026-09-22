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
        if guess_count == 1:
            feedback = "Amazing, you got it on your first guess!"
        elif guess_count <= 3:
            feedback = "Great job!"
        elif guess_count <= 5:
            feedback = "Good job!"
        else:
            feedback = "You got it! Keep practicing to guess it faster."

        guess_word = "guess" if guess_count == 1 else "guesses"
        print(f"{feedback} It took you {guess_count} {guess_word}.")
        break