import sys
sys.path.append('..')

import csv
import time
import json
import random
import argparse
from requirements import *
from graph_generator import graph_warper, GraphType


PATH = './data_openlab'
PROFILE = {
    'TEST': {
        'base': 100000,
        'start_pow': 1,
        'target_pow': 1,
        'repeat': 50,
    },
    'NODE': {
        'base': 2,
        'start_pow': 6,
        'target_pow': 16,
        'repeat': 200,
    }
}
#ALGOS = [get_clustering_coefficient, get_degree_distribution, get_diameter]
ALGOS = [get_degree_distribution]

parser = argparse.ArgumentParser(description='Benchmark Graph Algoritms')
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
            # input erdos random
            items = graph_warper(size, GraphType.ERDOS)
            #print(items)
            graph = Graph(size, items)
            # print('org items:', items)
            for algo in ALGOS:
                result, elapse_time = benchmark(algo, graph)
                print(f'\t\t\tAlgo: {algo.__name__}'.ljust(32), f'result: {result}'.ljust(32), f'Time: {elapse_time} ({elapse_time / (10 ** 9)} sec.)')
                name = f'{algo.__name__}_'
                save_data(name + 'result', size, result)
                #save_data(name + 'time', size, elapse_time)
        end_time = time.time()
        ep_time = end_time - start_time
        avg_time = (avg_time + ep_time) / 2
        print(f'\t\tAverage Time: {avg_time} sec.\t\tExpected finish time: {avg_time * (setting["repeat"] - re) / 60} min. ({avg_time * (setting["repeat"] - re) / 3600} hr.)')
        print()

# fix benchmark to work with my algorithm instead
def benchmark(algorithm: callable, Graph) -> int:
    # wall time - actuall time
    # cpu time - cycle time
    start_time = time.process_time_ns() # cpu time
    # just a graph of items
    result = algorithm(Graph)
    end_time = time.process_time_ns()
    elapse_time = end_time - start_time
    # print(assignments, free_space)
    return result, elapse_time


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