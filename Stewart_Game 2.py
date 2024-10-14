import random  # Import random number

def player_guess():
    number_to_guess = random.randint(1, 1000)  # Generates random number between 1 and 1000
    attempts = 10  # Limit number of chances

    print("Guess a number between 1 and 1000.") #Instructions for player
    print("You have 10 attempts.") #Attempts of player

    while attempts > 0: #Start loop if player has chances left
        guess = input("Guess: ") #Asks player for guess
        if guess.isdigit(): #Checks if guess is valid
            guess = int(guess) #Changes guess from string to integer
            attempts -= 1 #Reduces chances left by one
            if guess == number_to_guess: #Checks if guess is correct
                print("Congratulations!") #Congratulates player on correct guss
                return #End the function
            elif guess < number_to_guess: #Checks is guess is too low
                print("Too low.") #Informs player that guess is too low
            else: #Otherwise the guess is too high
                print("Too high.") #Informs player that guess is too high
            print(f"Attempts left: {attempts}") #Informs player of chances left
        else: #Determines that guess is not a number
            print("Invalid input.") #Informs player that guess is invalid

    print(f"Game over. The number was {number_to_guess}.") #Discloses to player the correct guess

def npc_guess(): 
    print("Think of a number between 1 and 1000.") #Tasks player to think of number between 1 and 1000
    input("Press Enter when ready...") #Asks player to press enter after they have chosen a nummber
    min_num = 1 #Limits lowest number to 1
    max_num = 1000 #Limits highest number to 1000
    attempts = 10 #Limits chances to 10

    while attempts > 0: #Start loop as long as attempts are more than 0
        guess = random.randint(min_num, max_num) #NPC thinks of number
        print(f"NPC guesses: {guess}") #Prints NPC's guess
        feedback = input("Higher (H), Lower (L), or Correct (C)? ").upper() #Asks player if their number is Higher, Lower or Correct
        attempts -= 1 #Reduces attempts by 1

        if feedback == "C": #Checks if player's response is C
            print("Congratulations!") #Prints congratulations for NPC
            return #End the function
        elif feedback == "H": #Indicates that feedback was too low
            min_num = guess + 1 #Adjusts minumum number of NPC for next guess
        elif feedback == "L": #Indicates that feedback was too high
            max_num = guess - 1 #Adjusts maximum number of NPC for next guess
        else: #Checks if input of player is invalid
            print("Invalid input.") #Informs player of invalid input

    print("Game over.") #Informs player that game is done

def play_game():
    while True: #Starts loop of game to allow player play multiple times 
        player_guess() #Calls palyer guessing function
        npc_guess() #Calls NPC guessing function
        play_again = input("Play again? (yes/no): ")  #Ask player if they want to play again
        if play_again.lower() != "yes": #Breaks loop if player doesn't want to play again
            break #Exits loop

play_game() #Starts game by calling the play_game function