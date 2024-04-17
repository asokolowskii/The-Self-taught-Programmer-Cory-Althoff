"""
Add a docstring to all of the functions you wrote in challenges 1–5.
"""

#Task 1
def num_square(x):
    """
    Takes an integer and returns that number squared.
    :param x: int.
    :return: int x squared.
    """
    return x ** 2

print(num_square(7))

#Task 2
def get_string(string):
    """
    Prints a given string.
    :param string: str
    """
    print(string)

get_string("That is so simple")

#Task 3
def equation(x, y, z, a=2, b=5):
    """
    Returns the result of an equation containing
    three required parameters and two optional parameters.
    :param x: int
    :param y: int
    :param z: int
    :param a: int
    :param b: int
    :return: int.
    """
    return x + a - (y * z) % b

print(equation(4,3, 7))

#Task 4
def division(a):
    """
    Returns the result of the integer divided by 2.
    :param a: int.
    :return: int a divided by 2.
    """
    return a / 2

b = division(18)
def multiply(b):
    """
    Returns the result of the integer multiplied by 4.
    :param b: int.
    :return: int b multiplied by 4.
    """
    return b * 4

print(multiply(b))

#Task 5
def convert(x):
    """
    Converts a string to a float and returns the result.
    :param x: str.
    :return: the number resulting from the conversion.
    """
    try:
        return float(x)
    except ValueError:
        print("You have just given a wrong type of value!")

print(convert("456"))
