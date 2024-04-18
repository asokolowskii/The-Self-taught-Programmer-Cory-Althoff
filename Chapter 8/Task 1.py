"""
Call a different function from the statistics module.
"""

import statistics

list = [2, 5, 19, 22, 47, 23, 88, 14]

print(statistics.geometric_mean(list))

print(statistics.harmonic_mean(list))

print(statistics.quantiles(list))