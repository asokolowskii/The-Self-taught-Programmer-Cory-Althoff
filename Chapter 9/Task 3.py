"""
Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority
Report"], ["Titanic", "The Revenant", "Inception"], ["Training
Day", "Man on Fire", "Flight"]] and write them to a CSV file. The data from
each list should be a row in the file, with each item in the list separated by a comma.
"""

import csv

list = [["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]

with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(list[0])
    write.writerow(list[1])
    write.writerow(list[2])

