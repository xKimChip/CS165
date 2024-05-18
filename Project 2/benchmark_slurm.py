import sys
sys.path.append('..')

import csv
import time
import json
import random
import argparse
from requirements import *


PATH = './data_openlab'
PROFILE = {
    'TEST': {
        'base': 2,
        'start_pow': 4,
        'target_pow': 15,
        'repeat': 10,
    },
    'NODE': {
        'base': 2,
        'start_pow': 4,
        'target_pow': 18,
        'repeat': 500,
    }
}
ALGOS = [next_fit, first_fit, first_fit_decreasing, best_fit, best_fit_decreasing]


parser = argparse.ArgumentParser(description='Benchmark Bin Packing Algos.')
parser.add_argument('profile', metavar='P', type=str, help='Profile', choices=PROFILE.keys())
args = parser.parse_args()
profile = PROFILE[args.profile]


def repeat_benchmark(setting: dict) -> None:
    avg_time = 0
    for re in range(setting['repeat']):
        print(f'\tREPEAT: {re + 1}')

        start_time = time.time()
        for po in range(setting['start_pow'], setting['target_pow'] + 1):
            base = setting['base']
            size = base ** po
            print(f'\t\tSize: {base}^{po} = {size}')

            items = [round(random.uniform(0, 0.7), 10) for _ in range(size)]
            # print('org items:', items)
            for algo in ALGOS:
                waste, elapse_time = benchmark(algo, items.copy())
                print(f'\t\t\tAlgo: {algo.__name__}'.ljust(32), f'waste: {waste}'.ljust(32), f'Time: {elapse_time} ({elapse_time / (10 ** 9)} sec.)')
                name = f'{algo.__name__}_'
                save_data(name + 'waste', size, waste)
                save_data(name + 'time', size, elapse_time)
        end_time = time.time()
        ep_time = end_time - start_time
        avg_time = (avg_time + ep_time) / 2
        print(f'\t\tAverage Time: {avg_time} sec.\t\tExpected finish time: {avg_time * (setting["repeat"] - re) / 60} min. ({avg_time * (setting["repeat"] - re) / 3600} hr.)')
        print()


def benchmark(algorithm: callable, items: list[float]) -> int:
    assignments = [0] * len(items)
    free_space = list()
    # wall time - actuall time
    # cpu time - cycle time
    start_time = time.process_time_ns() # cpu time
    algorithm(items, assignments, free_space)
    end_time = time.process_time_ns()
    elapse_time = end_time - start_time
    # print(assignments, free_space)
    return sum(free_space), elapse_time


def save_data(name: str, size: int, elapsed_time: int) -> None:
    file = f'{PATH}/{name}.csv'
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([size, elapsed_time])


if __name__ == '__main__':
    # if not os.path.exists(profile['path']):
    #     os.mkdir(profile['path'])

    data = dict()
    data['settings'] = profile
    data['start_time'] = time.ctime()
    start = time.time()
    repeat_benchmark(profile)
    data['finish_time'] = time.ctime()
    data['total_time'] = time.time() - start

    with open(f'{PATH}/0_DONE_{time.process_time_ns()}.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(json.dumps(data, indent=2))
    print('DONE!')