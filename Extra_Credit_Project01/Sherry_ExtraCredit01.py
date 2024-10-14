#Sherry_ExtraCredit01

import random

def play_game():
 
    # this gives a random number between 1-1000
    number_to_guess = random.randint(1, 1000)
    attempts_left = 10  # the maximum attempts to guess is 10 times
    
    print("I have selected a random number between 1 and 1000.")
    print("You have 10 attempts to guess the number.")

    # loop
    while attempts_left > 0:
        try:
            guess_input = input(f"\nEnter your guess (1 to 1000). You can type 'stop' at any time to quit. Attempts left: {attempts_left}: ").strip().lower()
            
            # check if player wants to stop the game
            if guess_input == "stop":
                print("You've chosen to stop the game. Goodbye!")
                return  # exit the current game loop
            
            guess = int(guess_input)

            # make sure the guess is valid
            if guess < 1 or guess > 1000:
                print("Invalid input! Please enter a number between 1 and 1000.")
                continue

            # tell the player if the number should be higher, lower, or correct
            if guess < number_to_guess:
                print("higher")
            elif guess > number_to_guess:
                print("lower")
            else:
                print("correct")
                break  # end the loop when the guess is correct

            attempts_left -= 1 

        except ValueError:
            # alternative when input is invalid
            print("Invalid input! Please enter a valid number or type 'stop' to quit.")
            continue

    # tell player that they run out of chances
    if attempts_left == 0 and guess != number_to_guess:
        print(f"\nYou've run out of attempts! The correct number was {number_to_guess}.")

# new game loop
print("Welcome to the Number Guessing Game!")

while True:
    play_game()

    # ask the player if they want to play again
    play_again = input("Enter 'play' to play again. You can enter 'stop' at any time to quit: ").strip().lower()

    if play_again != "play":
        print("Thank you for playing this game. ")
        break  # end game

