"""
Write a function that takes three required parameters and two optional parameters.
"""

def equation(x, y, z, a=2, b=5):
    return x + a - (y * z) % b

print(equation(4,3, 7))