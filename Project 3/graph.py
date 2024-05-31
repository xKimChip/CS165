# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
from collections.abc import Iterable
from collections import deque

class Graph:
    def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]
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
    
    def get_degree(self, node: int):
        return len(self.adj_list[node])
    
    def has_edge(self, u: int, w: int):
        return w in self.adj_list[u]
    


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


    def bfs(self, start: int) -> int:
        visited = [False] * self.num_nodes
        queue = deque([start])
        distances = [-1] * self.num_nodes
        distances[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    distances[neighbor] = distances[node] + 1

        return distances
    
    def degenerative_ordering(self):
        L = []
        dv = [self.get_degree(v) for v in range(self.get_num_nodes())]  # Initial degrees
        D = [[] for _ in range(self.num_nodes)]  # Array to track vertices by their degree
        
        
        for v, degree in enumerate(dv):
            D[degree].append(v)
        #print(D)
        k = 0
        
        for _ in range(self.num_nodes):  # Iterate over all vertices
            # Find the first non-empty D[i]
            for i in range(self.num_nodes):
                k = max(k, i)
                if D[i]:
                    break
            
            
            v = D[i].pop()  # Select and remove a vertex from D[i]
            L.append(v)  # Add v to the beginning of L
            
                    # Update the degrees of neighbors and reposition them in D
            for neighbor in self.adj_list[v]:
                if neighbor not in L:
                    old_degree = dv[neighbor]
                    dv[neighbor] -= 1
                    D[old_degree].remove(neighbor)
                    D[dv[neighbor]].append(neighbor)  

        return L, k  # Return the degeneracy ordering and the degeneracy value
            