# Example file: next_fit.py

# explanations for member functions are provided in requirements.py
import math
import sys

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.insert(0, 1)
    j = 0
    for x in range(len(items)):
        if free_space[j] - items[i] < sys.float_info.epsilon or free_space[j] > items[i]:
            assignment[i] = j
            free_space[j] -= items[i]
        else:
            free_space.insert(0,1)
            assignment[i] = j + 1
            free_space[j] -= items[j]



    pass