"""
Print each item in the list from the first challenge and their indexes.
"""

list =  ["The Walking Dead", "Entourage",
"The Sopranos", "The Vampire Diaries"]

for i, title in enumerate(list):
    print(str(title) + ", index: " + str(i))
