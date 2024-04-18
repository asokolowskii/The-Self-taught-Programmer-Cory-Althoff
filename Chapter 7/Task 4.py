"""
Write a program with an infinite loop (with the option to type q to quit)
and a list of numbers. Each time through the loop ask the user to guess a number
on the list and tell them whether or not they guessed correctly.
"""

from random import randint
list = [randint(1,10) for i in range(4)]

while True:
    a = input("Type q to quit the programme or press any key to continue: ")
    if a == "q":
        break

    try:
        guess = int(input("Guess a number on the list from 1 to 10: "))
    except ValueError:
        print("You can only enter numbers!")
        guess = int(input("Guess a number on the list from 1 to 10: "))
    if guess in list:
        print("You are correct!")
    else:
        print("You are incorrect! Try again!")
    print(list)