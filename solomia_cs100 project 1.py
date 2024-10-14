import random

def correct_number():
    correct_number = random.randint(1, 1000) #we generate a random number
    i = 10
    print("Guess the number I generated between 1 and 1000. 10 attempts left.")

    for attempt in range(1, i + 1): #making sure that the loop will run only 10 times, i is the number of attempts 
        guess = input(f"Attempt {attempt}/{i}: ")

        if not guess.isdigit():
            print("That's not a valid number. Please try again.")
            continue

        guess = int(guess) 

        if guess > correct_number:
            print("Too high!")
        elif guess < correct_number:
            print("Too low!")
        else:
            print(f"Correct")
            break
    else:
        print(f"You lost, the number is {correct_number}")

    if input("Play again (yes/no): ").lower() == 'yes':
        correct_number()

correct_number()

