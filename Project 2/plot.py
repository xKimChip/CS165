import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.metrics import r2_score


GROUP = False

LOGLOG = True
DATA_PATH = './data_openlab_node/'
SAVE_PATH = './plot/'

LABEL = {
    'waste': 'Average Waste',
    'time': 'Average Elapsed Time (nanoseconds)',
}

FILES = {
    'Next Fit Waste': {
        'file': 'next_fit_waste',
        'skip': 2
    },
    'First Fit Waste': {
        'file': 'first_fit_waste',
        'skip': 7
    },
    'First Fit Decreasing Waste': {
        'file': 'first_fit_decreasing_waste',
        'skip': 7
    },
    'Best Fit Waste': {
        'file': 'best_fit_waste',
        'skip': 7
    },
    'Best Fit Decreasing Waste': {
        'file': 'best_fit_decreasing_waste',
        'skip': 7
    },
    # 'Next Fit Time': {
    #     'file': 'next_fit_time',
    #     'skip': 2
    # },
    # 'First Fit Time': {
    #     'file': 'first_fit_time',
    #     'skip': 4
    # },
    # 'First Fit Decreasing Time': {
    #     'file': 'first_fit_decreasing_time',
    #     'skip': 4
    # },
    # 'Best Fit Time': {
    #     'file': 'best_fit_time',
    #     'skip': 4
    # },
    # 'Best Fit Decreasing Time': {
    #     'file': 'best_fit_decreasing_time',
    #     'skip': 4
    # },
}


DATA = {
    'Waste Comparison': {
        'xlabel': 'Input Size (n, # of elements)',
        'ylabel': LABEL['waste'],
        'files': [
            'Next Fit Waste',
            'First Fit Waste',
            'First Fit Decreasing Waste',
            'Best Fit Waste',
            'Best Fit Decreasing Waste'
        ]
    },
    # 'Time Comparison': {
    #     'xlabel': 'Input Size (n, # of elements)',
    #     'ylabel': LABEL['time'],
    #     'files': [
    #         'Next Fit Time',
    #         'First Fit Time',
    #         'First Fit Decreasing Time',
    #         'Best Fit Time',
    #         'Best Fit Decreasing Time'
    #     ]
    # },
    'FF Decreasing v.s. BF Decreasing (Waste)': {
        'xlabel': 'Input Size (n, # of elements)',
        'ylabel': LABEL['waste'],
        'files': [
            'First Fit Decreasing Waste',
            'Best Fit Decreasing Waste'
        ]
    },
    # 'FF Decreasing v.s. BF Decreasing (Time)': {
    #     'xlabel': 'Input Size (n, # of elements)',
    #     'ylabel': LABEL['time'],
    #     'files': [
    #         'First Fit Decreasing Time',
    #         'Best Fit Decreasing Time'
    #     ]
    # }
}


def load_data(file: str) -> dict:
    data = defaultdict(list)
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data[int(row[0])].append(float(row[1]))
    return data


def load_avg_data(file: str) -> tuple:
    data = load_data(file)
    sizes, avg_times = list(), list()
    sample_size = sum([len(v) for v in data.values()])

    for size, time in sorted(data.items()):
        sizes.append(size)
        avg_times.append(sum(time) / len(time))
    
    return sample_size, sizes, avg_times


def add_to_plot(file: str, label: str, loglog = True, skip = 0):
    sample_size, sizes, avg_times = load_avg_data(file)

    if loglog:
        x, y = sizes[skip:], avg_times[skip:]
        log_x, log_y = np.log(x), np.log(y)
        m, b = np.polyfit(log_x, log_y, 1)
        fit_func = np.poly1d((m, b))
        exp_y = fit_func(log_x)
        r2 = r2_score(log_y, exp_y)

        # print(fit_func)

        p = plt.loglog(sizes, avg_times, '.', base = 2, label=f'{label} Data Points')
        plt.loglog(x, np.exp(exp_y), '--', base = 2, color=p[-1].get_color(),
                # label=f'{label} #Fit: log C(n) ~ {m:.4f} log n + {b:.4f}, R^2 = {r2:.4f}',)
                label=f'{label} #Fit: log W(A) ~ {m:.4f} log n + {b:.4f}, R^2 = {r2:.4f}',)
        
        # print(f'{label}: log C(n) ~ {m:.4f} log n + {b:.4f}')

    else:
        x, y = sizes[skip:], avg_times[skip:]
        m, b = np.polyfit(x, y, 1)
        fit_func = np.poly1d((m, b))
        exp_y = fit_func(x)
        r2 = r2_score(y, exp_y)

        p = plt.plot(sizes, avg_times, '.-', label=f'{label} Data Points')
        plt.plot(x, exp_y, '--', color=p[-1].get_color(),
                label=f'{label} #Fit: C(n) ~ {m:.4f} n + {b:.4f}, R^2 = {r2:.4f}',)

        plt.gca().set_xscale('linear')
        plt.gca().set_yscale('linear')
    return sample_size



def plot_all():
    for label, data in FILES.items():

        plt.figure(figsize=(8, 5), dpi=150)
        plt.title(label=label, fontsize=12)
    
        sample_size = add_to_plot(DATA_PATH + data['file'] + '.csv', label, LOGLOG, data['skip'])
        plt.xlabel('Input Size (n, # of elements)')
        plt.ylabel(LABEL['waste' if 'waste' in data['file'] else 'time'])
        plt.legend(loc='upper left', fontsize=8)
        #plt.subplots_adjust(bottom=0.15)
        plt.text(0.05, 0.03, f'Sample Size: {sample_size} points. / Skip = {data["skip"]}', transform=plt.gcf().transFigure, fontsize = 8,
                bbox=dict(boxstyle = 'round', edgecolor = 'lightgray', facecolor = 'white'))
        plt.savefig(SAVE_PATH + label + '.png', dpi=300)
        plt.cla()


def plot_data():
    sample_size = 0
    for label, data in DATA.items():

        plt.figure(figsize=(8, 5), dpi=150)
        plt.title(label=label, fontsize=12)

        plt.xlabel(data['xlabel'])
        plt.ylabel(data['ylabel'])

        # plt.loglog(subset['Array Size'], subset['Time (ns)'], label=f'{algorithm} ~ {round(m,5)} log N + {round(b,5)}', marker='o')

        for file in data['files']:

            sample_size += add_to_plot(DATA_PATH + FILES[file]['file'] + '.csv', file, LOGLOG, FILES[file]['skip'])    

        plt.legend(loc='upper left', fontsize=8)
        #plt.subplots_adjust(bottom=0.15)
        plt.text(0.05, 0.03, f'Sample Size: {sample_size} points.', transform=plt.gcf().transFigure, fontsize = 8,
                bbox=dict(boxstyle = 'round', edgecolor = 'lightgray', facecolor = 'white'))
        plt.xscale('log',base=2)
        plt.yscale('log',base=2)
        plt.savefig(SAVE_PATH + label + '.png', dpi=300)
        
        plt.cla()


if __name__ == '__main__':
    if GROUP: plot_data()
    else: plot_all()