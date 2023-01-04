"""
Exercise "Number guessing"

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Create a program that will play a number guessing game with the user. The program works like this:
    Explain the rules to the user.
    Randomly generate a 4-digit integer number.
    Ask the user to guess a 4-digit number.
    Every digit that the user guesses correctly in the correct position, counts as a black coin.
    Every digit the user guesses correctly, but in the wrong position, counts as a white coin.
    After the user made a guess, print out how many black and white coins the guess is worth.
    let the user guess until the guess is correct.
    Keep track of the number of guesses the user makes throughout the game and print it out at the end.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import random
from random import randint

number = randint(1000, 10000)
answer = []

number = 1234


while number > 0:
    answer.append(number % 10)
    number = (number - number % 10) // 10
answer.reverse()

def break_into_digits(guess):

    j = []
    while guess > 0:
        j.append(guess % 10)
        guess = (guess - guess % 10) // 10

    j.reverse()
    print(f"You have guessed {j}!")
    return j


def check(j):
    print("check")
    set1 = j
    set2 = answer
    intersection1 =


def turn(guess):
    check(break_into_digits(guess))

round = 0
#     gamestart

print(f"Guess a 4 digit number, every digit you have correct and is in the correct position gives you a black coin, \n every digit you have correct but in the wrong position gives you a white coin")
print(f"The answer is {answer}!")
# guess = input()
guess = 1234
turn(guess)
# print(break_into_digits(guess))
# print(check(guessdigit))