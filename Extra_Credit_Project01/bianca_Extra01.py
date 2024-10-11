# Commented by Myo Thida 
# 2.5 out of 5 points. The program works as expected. However, the answer is printed out in the beginning of the game. This is not a good practice. No fun to play a game when you know the answer.
# Date: 10/10/2019

import random
import math

def guessingGame():
    correctAnswer = random.randint(1, 1000)
    userGuess = 0
    attemptsMade = 0
    print(correctAnswer)

    while userGuess != correctAnswer and attemptsMade < 10:
        userGuess = int(input("Enter an integer between 1 and 1000: "))
        attemptsMade += 1

        if userGuess == correctAnswer:
            print("Good Job!")
            break
        elif userGuess > correctAnswer:
            print("Too High!")
        elif userGuess < correctAnswer:
            print("Too Low!")
        else:
            print("Error :(")

    if userGuess != correctAnswer:
        print("Out of attempts. Better luck next time!")

def main():
    while True:
        guessingGame()
        playAgain = input("Play again? (Y/N)").upper()
        if playAgain != "Y":
            print("See you later, then?")
            break

if __name__ == "__main__":
    main()




