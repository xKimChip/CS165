# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
import copy
from collections.abc import Iterable

class Graph:
    def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]
        self.degen_list = None
        self.num_edges = len(edges)
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        # Node is second, 

    def get_num_nodes(self) -> int:
        return self.num_nodes

    def get_num_edges(self) -> int:
        return self.num_edges

    def get_neighbors(self, node: int) -> Iterable[int]:
        return self.adj_list[node]
    
    #def get_degree_list(self):
        
    
    def get_degen_list(self):
        
        degen_list = [] # Output list to store the degeneracy ordering
        D = [[] for _ in range(self.num_nodes)]  # Array to track vertices by their degree
        dv = { v: len(neighbors) for v, neighbors in self.adj_list }  # Initial degrees

        for v, degree in dv.items():
            D[degree].append(v)
        
        k = 1
        
        for _ in range(self.num_nodes):  # Iterate over all vertices
            # Find the first non-empty D[i]
            for i in range(k + 1):
                if D[i]:
                    break

            k = max(k, i)
            v = D[i].pop()  # Select and remove a vertex from D[i]
            degen_list.insert(0, v)  # Add v to the beginning of L 

            # Update the degrees of neighbors and reposition them in D
            for neighbor in self.adj_list[v]:
                if neighbor not in degen_list:
                    old_degree = dv[neighbor]
                    dv[neighbor] -= 1
                    D[old_degree].remove(neighbor)
                    D[dv[neighbor]].append(neighbor)  

        return degen_list, k  # Return the degeneracy ordering and the degeneracy value

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
