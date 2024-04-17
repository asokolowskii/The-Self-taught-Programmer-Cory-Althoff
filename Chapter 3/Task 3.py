"""
Write a program that prints a message if a variable is less than or equal to 10, another
message if the variable is greater than 10 but less than or equal to 25, and another message
if the variable is greater than 25.
"""

num = int(input("Put here any number: "))
if num <= 10:
    print("Your number is less than or equal to 10!")
elif num <= 25:
    print("Your number is greater than 10 but less than or equal to 25!")
else:
    print("Your number is greater than 25!")
