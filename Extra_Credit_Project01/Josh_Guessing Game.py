#Guessing Game
condition = True
while condition == True:
    print("hello this is a guessing game where you have 5 guesses to get the correct number I am thinking")
    print("The number will be between 1 and 1000 ")
    import random
    number = random.randint(1, 1000)
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
