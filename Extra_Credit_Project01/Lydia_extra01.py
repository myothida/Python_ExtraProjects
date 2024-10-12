print("The program will generate a random number between 1 and 1000, enter your guess to guess the number, youn will have 10 chances to guess the correct number")
import random

game = True
while (game == True):
    # Randomly generates a number in the range 1-1000,including the end points:
    number = random.randint(1, 1000)

    # Allow 10 guesses:
    guesses_given = 10
    while (guesses_given > 0):
        print("remaining chances you have:{}".format(guesses_given))
        # the players enter their guess:
        guess = input("enter a number between 1 to 1000:")
        guess = int(guess)

        # the game gives feedback:
        if (guess > 1000 or guess < 1):
            print("remaining chances you have:{}".format(guesses_given))
            print("Error!")
        elif (guess > number):
            print("Too high!")
            guesses_given = guesses_given - 1
        elif (guess < number):
            print("Too low!")
            guesses_given = guesses_given - 1
        elif (guess == number):
            print("Correct!")
            # congratulate the player
            print("congratulations!")
            break
      #choose to continue or end the game:
        if (guesses_given == 0):
            next = input("do you want to continue? input 0 continue, otherwise exit:")
            next = int(next)
            if (next == 0):
                game = True
            else:
                game = False
                print("Game Over")
                break
