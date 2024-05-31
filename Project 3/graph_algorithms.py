# explanations for these functions are provided in requirements.py

import operator
from graph import Graph



#We can use graph degeneracy to get the diameter of the graph I believe?
def get_diameter(graph: Graph) -> int:
    max_distance = 0
    for x in range(graph.get_num_nodes()):
        distances = graph.bfs(x)
        max_distance = max(max_distance, max(distances))
    return max_distance
    

def get_clustering_coefficient(graph: Graph) -> float:
    L, k = graph.degenerative_ordering()
    degenerated_list = degernative_list(graph, L)
    triangles = 0
    #for each vertex in the degenerate list
    for v in degenerated_list:
        for u in range(0,len(v)):
            for w in range(u,len(v)):
                if graph.has_edge(v[u], v[w]):
                    triangles += 1
    denominator = 0
    for v in range(0, graph.num_nodes):
        dv = graph.get_degree(v)
        denominator +=  dv * (dv - 1) / 2
    
    clustering_coefficient = (3 * triangles) / denominator
    return clustering_coefficient
        

            

    #return clustering


def get_degree_distribution(graph: Graph) -> dict[int, int]:
    deg_list = dict()
    for x in range(0, graph.get_num_nodes()):
        deg_list[graph.get_degree(x)] = deg_list.get(graph.get_degree(x), 0) + 1
    sorted_deg_list = dict(sorted(deg_list.items(), key=operator.itemgetter(0)))
    return sorted_deg_list
	

def degernative_list(graph: Graph, ordering: list):
    degenerated_list = [[] for _ in range(graph.num_nodes)]  
    placed = set()

    for v in ordering:
        for neighbor in graph.get_neighbors(v):
            if neighbor not in placed:
                degenerated_list[v].append(neighbor)

        placed.add(v)  

    return degenerated_list
