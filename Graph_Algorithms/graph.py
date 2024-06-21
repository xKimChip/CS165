# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
from collections.abc import Iterable
from collections import deque, defaultdict

class Graph:
    def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
        self.num_nodes = num_nodes
        self.adj_list = defaultdict(set)
        self.num_edges = 0
        for u, v in edges:
            self.num_edges += 1
            self.adj_list[u].add(v)
            self.adj_list[v].add(u)
        # Node is second, 

    def get_num_nodes(self) -> int:
        return self.num_nodes

    def get_num_edges(self) -> int:
        return self.num_edges

    def get_neighbors(self, node: int) -> Iterable[int]:
        return self.adj_list[node]
    
    def get_degree(self, node: int) -> int:
        return len(self.adj_list[node])
    
    def has_edge(self, u: int, w: int) -> int:
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
    
    def degenerative_ordering(self) -> Iterable[int]:
        L = deque()
        k = 0
        visited = set()
        dv = { v:len(n) for v, n in self.adj_list.items() }  # Initial degrees
        D = defaultdict(set)  # Array to track vertices by their degree
        Nv = defaultdict(set)
        
        for v, degree in self.adj_list.items():
            D[len(degree)].add(v)
        i = 0

        
        for _ in range(self.num_nodes):  # Iterate over all vertices
            # Find the first non-empty D[i]
            try:
                i = next(x for x in sorted(D.keys()) if len(D[x]) != 0)
            except:
                return Nv, k
            k = max(k, i)
            
            v = D[i].pop()  # Select and remove a vertex from D[i]
            L.appendleft(v)  # Add v to the beginning of L
            visited.add(v)
            
            # Update the degrees of neighbors and reposition them in D
            for neighbor in self.adj_list[v]:
                if neighbor not in visited:
                    D[dv[neighbor]].remove(neighbor)
                    dv[neighbor] -= 1
                    D[dv[neighbor]].add(neighbor)
                    Nv[v].add(neighbor)

                

        return Nv, L, k  # Return the degeneracy ordering and the degeneracy value

    def count_triangles(self) -> int:
        Nv, L, _ = self.degenerative_ordering()  # Obtain the degenerative ordering
        triangle_count = 0


        for v in list(Nv.keys()):  # Process vertices in the ordering
            for u in Nv[v]:
                for w in Nv[v]:
                    if u != w and u in Nv[w]:
                        triangle_count += 1

        return triangle_count



    def degernative_list(self, ordering: list) -> Iterable[int]:
        degenerated_list = [[] for _ in range(self.num_nodes)]  
        placed = set()

        for v in ordering:
            for neighbor in self.get_neighbors(v):
                if neighbor not in placed:
                    degenerated_list[v].append(neighbor)

            placed.add(v)  

        return degenerated_list       