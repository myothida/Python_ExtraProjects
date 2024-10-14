#Guessing Game
# (2.5 points out of 5 points)
# (1 point): The game successfully generates a random number and allows the player to guess it, providing feedback if the guess is too high or too low.
# (1 point): The code checks if the guess is an integer between 0 and 1000.
# (0.5 point): The player is prompted to decide whether to play again after winning or losing. But, the code does not end correctly if you enter 0. 
# (comment) - Your code does not work if I won the game with less than 10 guesses and want to stop playing. It will keep asking me to play again.
# Check Josh.png
# (0 point): The game did not end correctly after running the 2nd round.
# (0 point): The comments are not added to the code.



condition = True
while condition == True:
    print("hello this is a guessing game where you have 5 guesses to get the correct number I am thinking")
    print("The number will be between 1 and 1000 ")
    import random
    number = random.randint(1, 1000)
    print(number)
    count = 0
    while count< 10 :
        guess = (input("guess the number: "))
        if guess.isdigit():
            if int(guess) > number:
                print("Too high!")
            elif int(guess) < number:
                print("Too low!")
            elif int(guess) == number:
                print("Correct!")
                startOver = (input("play again? if yes type 1: "))
                if int(startOver) != 1:
                    condition = False

        else:
            print("numbers only man!")
        count += 1
    if count == 10:
        print("game over")
        print("the number was", number)
        startOver = (input("play again? if yes type 1: "))
        if int(startOver) != 1:
            condition = False
