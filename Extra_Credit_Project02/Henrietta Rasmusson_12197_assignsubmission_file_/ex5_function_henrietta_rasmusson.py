# -*- coding: utf-8 -*-
"""Ex5_Function_Henrietta_Rasmusson.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mHphiIRSskNTJd2vTtlXikTue4jbW5-I

Exercises are taken from : https://www.brianheinold.net/python/A_Practical_Introduction_to_Python_Programming_Heinold.pdf

Ex 1: Write a function called rectangle that takes two integers m and n as arguments and prints
out an m× n box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****
"""

def rectangles(m,n):
  """
  rectangles, creates a rectangle out of asterisks of a given number or rows and columns
  Args :
  m (int) : number of rows in the rectangle
  n (int) : number of columns in the rectangle
  Returns :
  No value returned, just printed during the function
  """
  m = int(m)
  n = int(n)
  h = 0
  l = 0
  while h < m :    #loops for the number of rows
    print("*"*n)   #Prints out a row of stars of stars
    h += 1

rectangles(2,4)

"""Ex 2: Write a function that takes an integer n and returns a random integer with exactly n digits. For
instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
that is really 93, which is a two-digit number.
"""

def random_int(n):
  """
  random_int, generates a random number n digits long
  Args :
  n (int) : length of the number that will be generated
  Returns :
  num (int) : A randomly generated number n digits long
  """
  import random
  n = int(n)
  num = 0
  count = 0
  while count < n:                  #runs until the number of digits that have been generated so far equal n
    if(count == n-1):
      temp = random.randint(1,9)      #Generates a random number 1,9 making sure it is not 0 so the number does not start with 0
      num += temp*10**count           #puts it in the correct digit position
      count += 1
    else :
      temp = random.randint(0,9)     #Generates a number 0,9 as it is not the first digit
      num += temp*10**count         #puts it in the correct digit position
      count += 1
  return num

print(random_int(3))

"""Ex 3: Write a function called number_of_factors that takes an integer and returns how many
factors the number has.
"""

def number_of_factors(num):
  """
  number_of_factors, find the number of factors a given number has
  Args :
  num (int) : the number which is having its number of factors found
  Returns :
  count (int) : the number of factors of the given number num
  """
  num = int(num)
  count = 0
  test = 1
  while test <= num:        #goes through all numbers less than num
    if(num%test == 0):      #find if test is a factor of num
      count += 1            #counts the number of factors found
    test += 1
  return count
print(number_of_factors(21))

"""Ex4: Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1.Ignore the case in your function. It means h and H are the same.
"""

def first_diff(first,second):
  """
  first_diff, find the first difference between two strings and returns the index of the difference, or if there is no difference returns -1
  Args :
  first (string) : the first string of the two being compared
  second (string) : the second string of the two being compared
  Returns :
  count (int) : the index where the first difference bewteen the two string occur
  or -1 if there is no difference between the two strings
  """
  count = 0
  check = False
  if len(first) < len(second): #find shortest string
    first1 = first
    second1 = second
  else :
    first1 = second
    second1 = first
    check = True
  while count < len(first1):                              #go through all letters in the shortest string
    if first[count].lower() != second[count].lower() :    #checks if letters are the same, after changing them both to lowercase
      return count
    count += 1
  if check == False:                                      #If there are no differences return -1
      return -1
  else :                                                  #If there are differences return the index of the difference
    return count
print(first_diff("Helloo","HEllo"))

"""Ex5: Write a function called root that is given a number x and an integer n and returns x/n. In
the function definition, set the default value of n to 2.
"""

def root(x,n=2): #was it supposed to be x/n
  """
  root, divides two given values
  Args :
  x (int) : the dividend in the equation
  n (int) : the divisor in the equation, and is by default 2
  Returns :
  div (float) : quotient of the two values x and n
  """
  x = int(x)
  n = int(n)
  div = x/n    #x divided by n
  return div   #return the answer

print(root(10))

def root(x,n=2): #or was it supposed to be nth root of x
  """
  root, finds the nth root of x
  Args :
  x (int) : the value which the nth root will be found of
  n (int) : the index of the root, and is by default 2
  Returns :
  pow (float) : the value of the nth root of x
  """
  import math
  x = int(x)
  n = int(n)
  pow = math.pow(x, 1/n)   #calculates the nth root of x
  return pow               #returns the nth root of x

print(root(4))

"""Ex6: Write a function that solves the system of equations ax + by = e and cx +dy = f. Your function should takes 6 parameters, (a, b, c, d, e,f) and return the values of x and y. #EXTRA CREDIT"""

def equation_solver(a,b,c,d,e,f): #EXTRA CREDIT
  #Check the answer. 
  """
  equation_solver, solves the equations ax + by = e and cx +dy = f for x and y, given the values of a, b, c, d, e, f
  Args :
  a (int) : the value of a from the equation ax + by = e
  b (int) : the value of b from the equation ax + by = e
  c (int) : the value of c from the equation cx + dy = f
  d (int) : the value of d from the equation cx + dy = f
  e (int) : the value of e from the equation ax + by = e
  f (int) : the value of f from the equation cx + dy = f
  Returns in format (x,y) TUPLE:
  x (float) : the value of x from the equations ax + by = e and cx +dy = f
  y (float) : the value of y from the equations ax + by = e and cx +dy = f
  """
  a = int(a)
  b = int(b)
  c = int(c)
  d = int(d)
  e = int(e)
  f = int(f)
  x = ((f*b)-(d*e))/((b*c)-(d*a)) #Calculates x
  y = (e-a*x)/b                   #calculates y
  return x, y                     #returns x and y

print("(x, y)",equation_solver(1,1,5,4,1,1))

"""Ex7:  Write a function called change_case that given a string, returns a string with each upper  case letter replaced by a lower case letter and vice-versa. #EXTRA CREDIT"""

def change_case(word):   #EXTRA CREDIT
  """
  change_case, switches the case of a string so uppercase becomes lowercase and vice-versa
  Args :
  word (string) : the string which will have its case swapped
  Returns :
  the original string with the case of each letter swapped so that uppercase becomes lowercase and vice-versa
  """
  return word.swapcase()   #Swaps the case of the string then returns the swapped string

print(change_case("PigEOns"))

"""Ex8:  Write a function called primes that is given a number n and returns a list of the first n  primes. Let the default value of n be 100. #EXTRA CREDIT"""

def primes(n = 100):  #EXTRA CREDIT
  """
  primes, finds the first n number of primes not including 1
  Args :
  n (int) : the number of primes which will be found, is by default 100
  Returns :
  prim (list) : a list of n number of primes in ascending order
  """
  from sympy import isprime
  count = 0
  temp = 0
  prim = []
  while count < n:           #runs until n prime numbers have been found
    temp += 1
    if isprime(temp) :      #checks if the nuber is prime
      count += 1
      prim.append(temp)     #Adds the prime number to the list of primes
  return prim               #returns the list of primes

print(primes(10))

"""Ex9: ATic-tac-toe board can be represented be a 3×3 two-dimensional list, where zeroes stand for  empty cells, ones stand for X’s and twos stand for O’s. Write a function that is given such a list and randomly chooses a spot in which to place  a **2** (O). The spot chosen must currently be empty and a spot must be chosen. EXTRA CREDIT"""

def find_spot(grid):  #EXTRA CREDIT
  """
  find_spot , given a 3x3 grid, the code randomly finds empty position to add a 2(O)
  Args :
  grid (two-dimensional list) : the tick-tack-toa grid, where ones stand for X’s and twos stand for O’s, and 0's stand for empty spaces
  Returns :
  grid (two-dimensional list) : the same grid as entered into the function, but with one empty space randomly replaced by a 2 (O)
  """
  import random
  guess = []
  nrow = 0
  for l in grid:                            #check the grid for rows and columns
    nrow += 1
    for spot in l :
      if spot != 1 and spot != 2:           #checks if individual spots are free
        guess.append(True)
      else :
        guess.append(False)
  tot = 0
  fin = random.randint(0,len(guess)-1)
  while guess[fin] == False:
     fin = random.randint(0,len(guess))
  row = fin//nrow
  col = fin%nrow
  grid[row][col] = 2                        #Sets the randomly chosen free spot to 2
  return grid

find_spot([[2,0,1],[1,0,1],[0,1,0]])