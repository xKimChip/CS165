# explanations for these functions are provided in requirements.py

import operator
from graph import Graph



#We can use graph degeneracy to get the diameter of the graph I believe?
def get_diameter(graph: Graph) -> int:
    max_distance = 0
    distances = graph.bfs(0)
    while(1):
        #largest_distance = 0
        r = 0
        for i in range(0, len(distances)):
            if distances[i] > distances[r]:
                r = i
        if distances[r] > max_distance:
            max_distance = distances[r]
            distances = graph.bfs(r)
        else:
            break
    return max_distance
    


def get_clustering_coefficient(graph: Graph) -> float:
    triangle_count = graph.count_triangles() 
    denominator = 0
    for v in range(0, graph.num_nodes):
        dv = graph.get_degree(v)
        denominator +=  dv * (dv - 1) / 2
    
    clustering_coefficient = (3 * triangle_count) / denominator
    return clustering_coefficient
        
    



def get_degree_distribution(graph: Graph) -> dict[int, int]:
    deg_list = dict()
    for x in range(0, graph.get_num_nodes()):
        deg_list[graph.get_degree(x)] = deg_list.get(graph.get_degree(x), 0) + 1
    sorted_deg_list = dict(sorted(deg_list.items(), key=operator.itemgetter(0)))
    return sorted_deg_list
	
