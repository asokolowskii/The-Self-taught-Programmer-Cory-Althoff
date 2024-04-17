"""
Write a function that converts a string to a float and returns the result.
Use exception handling to catch the exception that could occur.
"""

def convert(x):
    try:
        return float(x)
    except ValueError:
        print("You have just given a wrong type of value!")

print(convert("456"))