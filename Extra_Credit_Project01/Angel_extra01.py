import random

# (1.5 points out of 5 points)
# (1 point): The game successfully generates a random number and allows the player to guess it, providing feedback if the guess is too high or too low.
# (0 point): The code did not correctly check if the guess is an integer between 0 and 1000.
# (0 point): The game did not end correctly after either winning or losing.
# (0 point): The player is not prompted to decide whether to play again after winning or losing.
# (0.5 point): The comments are added to the code, but they are not clear and do not explain the code.

game = True
while(game==True):
#generating a random number
    num = random.randint(1, 1000)
    print("This is a game where you guess the number generated randomly. After you enter a number, a feedback will be given. You have ten chances to try, good luck!")
 
    #Setting the rounds
    round = 10
    while (round>0):
        print("There is {} chance left!".format(round))
        #Asking for a guess
        guess = input("Enter your guess of the number between 1 and 1000: ")
        guess = int(guess)
        #Giving a feedback on the guess
        if(guess > 1000 or guess<1):
            print("There is {} chance left!".format(round))
            print("Error!")
        elif(guess > num):
            print("Too high!")
            round = round-1
        elif(guess < num):
            print("Too low!")
            round = round-1
        elif(guess == num):
            print("Correct!")
            round = -1
            break
        
        #Restart your game when winning
            restart = input("You win! Enter '1' if retry, enter anything else if end the game: ")
            restart = int(restart)
            if (restart==1):
                game=True
                break
            else:
                game=False
                round=-2
                print("Game End")
            break
    
                        
    #Restart the game when losing
    while (round==0):
        restart = input("You lose! Enter '1' if retry, enter anything else if end the game: ")
        restart = int(restart)
        if (restart==1):
            game=True
            break
        else:
            game=False
            round=-2
            print("Game End")
