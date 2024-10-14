# Author: Artem Tkachuk (4 out of 5 points)
# Comments: 
# (1 point) The game successfully generates a random number and allows the player to guess it, providing feedback if the guess is too high or too low.
# (1 point): The code correctly checks if the guess is an integer between 0 and 1000.
# (1 point): After winning or losing, the player is prompted to decide whether to play again.
# (1 point): The game ends correctly after either winning or losing
# (0 point): The condition while Answer.lower() != "yes" or Answer.lower() != "no" is not efficient way of handling this, though it works.

from random import randint #Generates random number from 0 to 1000
myRandomNumber = randint(0,1000)
i = 0
while i != 10: #loop while will work until 10 attempts will run out
  i = i+1 
  guess=input("Enter your guess: ") #Player can enter his guessing number
  try:
    if int(guess) > 1000 or int(guess) < 0:
      print("Enter number between 0 and 1000")
      i = i-1 #If the value is invalid, it won't count as an attempt to guess the number
      continue
    if i == 10 and myRandomNumber!=int(guess): # If all 10 attempts were used 
                                               # and the player didn't guess the number,
                                               # the game is over
      print("You lost") 
      print("The number was: ", myRandomNumber)
      Answer = input("Do you wanna play again? Yes/No: ") # asking whether player wants to play again or not
      while Answer.lower() != "yes" or Answer.lower() != "no" :
        if Answer.lower() == "yes": # Continues the game
          myRandomNumber = randint(0, 1000)
          i = 0
          break
        if Answer.lower() == "no": # Exits the game
          break
        else: #Incorrect value will return to the same question whether player wants to play again or not
          Answer=input("Enter correct value('Yes' to continue and 'No' to exit the game): ")
          continue
      if Answer.lower() == "no": # Exits the game
        break
    elif int(guess) > myRandomNumber: #If the guessed number is greater than actual one...
      print("Too high, try again!")
      continue
    elif int(guess) < myRandomNumber: #If the guessed number is lower than actual one...
      print("Too low, try again!")
      continue
    if int(guess) == myRandomNumber:
      print("Correct!\nCongratulations! You won!") # If the guessed number is equal to the actual one
                                                   # program will congratulate player
      Answer = input("Do you wanna play again? Yes/No: ")  # asking whether player wants to play again or not
      while Answer.lower() != "yes" or Answer.lower() != "no" :
        if Answer.lower() == "yes": # Continues the game
          myRandomNumber = randint(0, 1000)
          i = 0
          break
        if Answer.lower() == "no": # Exits the game
          break
        else: # Invalid value will return to the same question whether player wants to play again or not
          Answer=input("Enter correct value('Yes' to continue and 'No' to exit the game): ")
          continue
      if Answer.lower() == "no": # Exits the game
        break
  except ValueError: #Invalid value will return player to guess the number again
    print("Enter correct value (integer from 0 to 1000)")
    i=i-1
    continue
