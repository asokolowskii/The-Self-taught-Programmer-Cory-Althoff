"""
Lists, tuples, and dictionaries are just a few of the containers built into Python.
Research Python sets (a type of container). When would you use a set?
"""
#Sets are used to store multiple items in a single variable.

#The major difference is that sets, unlike lists or tuples,
#cannot have multiple occurrences of the same element and store unordered values.
new_set = {1 ,2, 3 , 4, 5, 6, 9}
print(new_set)

#list to set conversion
words = set(["a", "b", "c", "d"])
print(words)

new_set.add(7)
print(new_set)

new_set.remove(2)
print(new_set)

#Because sets cannot have multiple occurrences of the same element,
#it makes sets highly useful to efficiently remove duplicate values
#from a list or tuple and to perform common math operations like unions
#and intersections.