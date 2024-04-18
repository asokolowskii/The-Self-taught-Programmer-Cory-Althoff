"""
Take the string "Where now? Who now? When now?" and call a method that
returns a list that looks like: ["Where now?", "Who now?", "When now?"].
"""

string = "Where now?, Who now?, When now?"
string = string.split(" ?")
print(string)