"""
Write a program that asks a user a question, and saves their answer to a file.
"""

answer = input("What is your favourite music band? ")
with open("fav_band.txt", "w") as f:
    f.write("Your answer has been saved: " + answer)

with open("fav_band.txt", "r") as f:
    r = f.read()
    print(r)
