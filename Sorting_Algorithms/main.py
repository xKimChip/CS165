# Import each one of your sorting algorithms below as follows:
# Feel free to comment out these lines before your algorithms are implemented.
#import sys
import random
import csv
import time
import math
#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
import argparse
import copy

from pathlib import Path
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort1 import hybrid_sort1
from hybrid_sort2 import hybrid_sort2
from hybrid_sort3 import hybrid_sort3

def generate_random_list(size, permutation):
    num_list = list(range(1, size + 1))     #benchmark runs use py ./\benchmark.py SORT_NAME n
    if (permutation  == 1):
        random.shuffle(num_list)
    elif(permutation == 2):
        for i in range(int(math.log(len(num_list)))):
            n = len(num_list)
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            num_list[a], num_list[b] = num_list[b], num_list[a]
    elif(permutation == 3):
        num_list.reverse()
    return num_list

#store algorithm in 
Algorithms = {
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "shell_sort1": shell_sort1,
    "shell_sort2": shell_sort2,
    "shell_sort3": shell_sort3,
    "shell_sort4": shell_sort4,
    "hybrid_sort1": hybrid_sort1,
    "hybrid_sort2": hybrid_sort2,
    "hybrid_sort3": hybrid_sort3
}  

parser = argparse.ArgumentParser(description='Sort Benchmark')
parser.add_argument('--rangeBot', type=int, default=10, help='The bottom range of the array size')
parser.add_argument('--rangeTop', type=int, default=16, help='The top range of the array size')
parser.add_argument('--permutation', type=int, default=1, help='The number of permutations to generate')

if __name__ ==  "__main__":
    args = parser.parse_args()

    # create a csv file to write the results to
    directory = Path('results')
    csv_file = directory / 'hybridbend.csv'

    ## we will test all arrays size 2^rangeBot to 2^rangeTop
    arrLen = 2**args.rangeBot

    # write the header to the csv file
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Algorithm', 'Array Size', 'Time (ns)'])

        while(arrLen <= 2**args.rangeTop):
            # we want to run each test 10 times, we need to generate a list for each test
            # to ensure varying results
            print(arrLen)
            for i in range(10):
                nums_arr = generate_random_list(arrLen, args.permutation)
                # iterate through each algorithm and time how long sorting takes for curr
                # size array, we will run each test 10 times
                nums = copy.deepcopy(nums_arr)
                start_time = time.process_time_ns()
                Algorithms["hybrid_sort1"](nums_arr)
                end_time = time.process_time_ns()
                sort_time = end_time - start_time
                writer.writerow(["hybrid_sort1", arrLen, sort_time])
                nums = copy.deepcopy(nums_arr)
                start_time = time.process_time_ns()
                Algorithms["hybrid_sort2"](nums_arr)
                end_time = time.process_time_ns()
                sort_time = end_time - start_time
                writer.writerow(["hybrid_sort2", arrLen, sort_time])
                nums = copy.deepcopy(nums_arr)
                start_time = time.process_time_ns()
                Algorithms["hybrid_sort3"](nums_arr)
                end_time = time.process_time_ns()
                sort_time = end_time - start_time
                writer.writerow(["hybrid_sort3", arrLen, sort_time])
                nums = copy.deepcopy(nums_arr)
                start_time = time.process_time_ns()
                Algorithms["merge_sort"](nums_arr)
                end_time = time.process_time_ns()
                sort_time = end_time - start_time
                writer.writerow(["merge_sort", arrLen, sort_time])
                
                #for algorithm in Algorithms:
                #    nums = copy.deepcopy(nums_arr)
                #    start_time = time.process_time_ns()
                #    Algorithms[algorithm](nums)
                #    end_time = time.process_time_ns()
                #    # calculate the source time and write to csv
                #    sort_time = end_time - start_time
                #    # write results to the file
                #    writer.writerow([algorithm, arrLen, sort_time])
            arrLen *= 2








# Please read the below carefully:

# - Each sorting algorithm should be implemented in its own file.
# - No file should include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - Each function should modify the input list so that it is sorted upon completion.

# Note:
#   If your Shellsort and/or hybrid merge sort variants largely use the same code,
#   you may choose to implement them in a single file, and import them as follows:
# from shell_sort import shell_sort1, shell_sort2, shell_sort3, shell_sort4
# from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3
