"""
Write a program with two functions. The first function should take an integer
as a parameter and return the result of the integer divided by 2.
The second function should take an integer
as a parameter and return the result of the integer multiplied by 4.
Call the first function, save the result as a variable,
and pass it as a parameter to the second function.
"""

def division(a):
    return a / 2

b = division(18)
def multiply(b):
    return b * 4

print(multiply(b))