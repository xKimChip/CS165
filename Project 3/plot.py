import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.metrics import r2_score

GROUP = True

LOGLOG = True
DATA_PATH = './data_openlab_node/'
SAVE_PATH = './plot/'

FILES = {
    'Barabasi Albert': {
        'file': 'next_fit_waste',
        'skip': 2
    },
    'Erdos Renyi': {
        'file': 'first_fit_waste',
        'skip': 7
    }
}