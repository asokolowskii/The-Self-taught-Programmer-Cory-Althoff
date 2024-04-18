"""
Write a program that collects two strings from a user, inserts them into the string
"Yesterday I wrote a [response_one]. I sent it to [response_two]!"
and prints a new string.
"""

response_one = input("Give me the first word: ")
response_two = input("Give me the second word: ")

sentence = """Yesterday I wrote a {}. I sent it to {}!"""\
    .format(response_one, response_two)
print(sentence)