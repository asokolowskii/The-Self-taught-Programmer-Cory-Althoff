"""
Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list
[9, 1, 33, 83], and append each result to a third list.
"""

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
mult_list = []

for i in list1:
    for j in list2:
        mult_list.append(i * j)

print(mult_list)