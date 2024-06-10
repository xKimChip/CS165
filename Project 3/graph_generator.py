import math
import random
from enum import Enum
from graph import Graph


class GraphType(Enum):
    ERDOS = 'erdos'
    BARABASI = 'barabasi'


# p = 2 * math.log(n) / n
def erdos_renyi_random(n: int, p: float) -> set[tuple]:
    edges = set()
    u, w = 1, -1
    while u < n:
        w = w + 1 + math.floor(math.log(1 - random.random()) / math.log(1 - p))
        while w >= u and u < n:
            w, u = w - u, u + 1
        if u < n:
            edges.add((u, w))
    return edges


# d = 5
def barabasi_albert_random(n: int, d: int) -> set[tuple]:
    edges_chosen = dict()
    for v in range(0, n):               # for v = 0, ..., n - 1 do
        for i in range(0, d):           # for i = 0, ..., d - 1 do
            c = 2 * (v * d + i)
            edges_chosen[c] = v
            edges_chosen[c + 1] = edges_chosen[random.randint(0, c)]
    edges = set()
    for i in range(0, n * d):
        edges.add((edges_chosen[2 * i], edges_chosen[2 * i + 1]))
    return edges


def graph_warper(n: int, graph_type: GraphType) -> set[tuple]:
    if graph_type == GraphType.ERDOS:
        return erdos_renyi_random(n, 2 * math.log(n) / n)
    elif graph_type == GraphType.BARABASI:
        return barabasi_albert_random(n, 5)
