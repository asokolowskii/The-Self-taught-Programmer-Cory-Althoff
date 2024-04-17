"""
Write a program that lets the user ask your height, favorite color, or favorite author, and
returns the result from the dictionary you created in the previous challenge.
"""


personal_data = {"height": "172", "fav_color": "blue",
                 "fav_author": "George R.R. Martin", "weight": "60"}

answer = input("Provide values for the keys: height, fav_color, fav_author and weight ")
if answer in personal_data:
    print(personal_data[answer])

