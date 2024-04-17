"""
Write a program with a variable age assigned to an integer that prints different strings
depending on what integer age is.
"""

age = int(input("Put here any number: "))
if age < 18:
    print("You are just a kid!")
elif age <=65:
    print("You are an adult!")
else:
    print("You are an elder!")