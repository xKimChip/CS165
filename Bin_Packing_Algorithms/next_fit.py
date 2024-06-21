# Example file: next_fit.py

# explanations for member functions are provided in requirements.py
import sys
from math import fabs

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.append(1)
    j = 0
    for i in range(len(items)):
        if fabs(free_space[j] - items[i]) < sys.float_info.epsilon or free_space[j] > items[i]:
            assignment[i] = j
            free_space[j] -= items[i]
        else:
            free_space.append(1)
            j += 1
            assignment[i] = j
            free_space[j] -= items[i]
    pass