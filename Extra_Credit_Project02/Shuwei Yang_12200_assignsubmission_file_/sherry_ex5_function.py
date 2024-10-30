# -*- coding: utf-8 -*-
"""Sherry_Ex5_Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l6HX6Bw1nwbYPfEPRIjXBZXKLAS4D72u

Exercises are taken from : https://www.brianheinold.net/python/A_Practical_Introduction_to_Python_Programming_Heinold.pdf

Ex 1: Write a function called rectangle that takes two integers m and n as arguments and prints
out an m× n box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****
"""

def rectangle(m, n):
  for _ in range(m):
    print("*" * n)

# Example usage
rectangle(2, 4)

"""Ex 2: Write a function that takes an integer n and returns a random integer with exactly n digits. For
instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
that is really 93, which is a two-digit number.
"""

import random

def random_dig(n):
    if n == 1:
        return random.randint(0, 9)

    x = random.randint(10**(n-1), 10**n - 1)
    return x

# Example usage
print(random_dig(3))  # This will print a random 3-digit number

"""Ex 3: Write a function called number_of_factors that takes an integer and returns how many
factors the number has.
"""

def number_of_factors(N):
    if N < 1:
        return 0  # No factors for numbers less than 1

    factor_count = 0
    for d in range(1, int(N**0.5) + 1):
        if N % d == 0:
            factor_count += 1  # Count the divisor
            if d != N // d:  # Count the complementary divisor if it's different
                factor_count += 1

    return factor_count

# Example usage
print(number_of_factors(4))   # Output: 3 (Factors are 1, 2, 4)
print(number_of_factors(12))  # Output: 6 (Factors are 1, 2, 3, 4, 6, 12)
print(number_of_factors(1))   # Output: 1 (Factor is 1)
print(number_of_factors(-5))  # Output: 0 (Negative numbers have no positive factors)

"""Ex4: Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1.Ignore the case in your function. It means h and H are the same.
"""

def first_diff(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        if str1[i] != str2[i]:
            return i

    if len(str1) == len(str2):
        return -1

    return min_length

# Example usage:
print(first_diff("Chocolate", "chocolate"))
print(first_diff("Chocolate", "Chocolatte"))
print(first_diff("Chocolate", "Chocola"))
print(first_diff("Chocolate", "Chococlate"))

"""Ex5: Write a function called root that is given a number x and an integer n and returns x/n. In
the function definition, set the default value of n to 2.
"""

def root(x, n=2):
    return x / n

#Example Usage
result_default = root(10)  # Uses the default n=2
print(result_default)  # Output: 5.0

result_custom = root(10, 5)  # Uses n=5
print(result_custom)  # Output: 2.0

"""Ex6: Write a function that solves the system of equations ax + by = e and cx +dy = f. Your function should takes 6 parameters, (a, b, c, d, e, f) and return the values of x and y."""

def solve_system_of_equations(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        return None

    x = (e * d - b * f) / determinant
    y = (a * f - e * c) / determinant
    return x, y

"""Ex7:  Write a function called change_case that given a string, returns a string with each upper  case letter replaced by a lower case letter and vice-versa"""

def change_case(input_string):
    return input_string.swapcase()

#Example
original_string = "How much Wood would a Woodchuck Chuck if a Woodchuck ould Chuck Wood"
changed_string = change_case(original_string)
print(changed_string)

"""Ex8:  Write a function called primes that is given a number n and returns a list of the first n  primes. Let the default value of n be 100."""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n=100):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

# Example usage:
first_100_primes = primes()
print(first_100_primes)

"""Ex9: A Tic-tac-toe board can be represented be a 3×3 two-dimensional list, where zeroes stand for  empty cells, ones stand for X’s and twos stand for O’s. Write a function that is given such a list and randomly chooses a spot in which to place  a 2 (O). The spot chosen must currently be empty and a spot must be chosen."""

import random

def place_O(board):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

    if empty_spots:
        chosen_spot = random.choice(empty_spots)
        board[chosen_spot[0]][chosen_spot[1]] = 2
    else:
        print("no empty spot")

# Example usage:
tic_tac_toe_board = [
    [1, 2, 1],
    [0, 0, 0],
    [2, 1, 0]
]

place_O(tic_tac_toe_board)
print(tic_tac_toe_board)

"""Ex10:  Write a function that is given a 9 × 9 potentially solved Sudoku and returns True if it is solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are
 no repeated numbers in any row or any column or in any of the nine “blocks.”

"""

def is_valid_sudoku(board):
    for i in range(9):
        if len(set(board[i])) < 9 or len(set(board[j][i] for j in range(9))) < 9:
            return False
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            if len(set(board[r+i][c+j] for i in range(3) for j in range(3))) < 9:
                return False
    return True