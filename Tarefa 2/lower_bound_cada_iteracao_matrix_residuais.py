from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.flow = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.lower_bound = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, z, w):
        self.adj[u][v] = w
        self.lower_bound[u][v] = z

    def bfs(self, s, t, parent):
        visited = [False for _ in range(self.V)]
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.V):
                if not visited[v] and self.adj[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == t:
                        return True

        return False

    def edmonds_karp(self, source, sink):
        parent = [-1 for _ in range(self.V)]
        max_flow = 0

        residual_graphs = []
    
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            path = []
    
            while s != source:
                path_flow = min(path_flow, self.adj[parent[s]][s])
                path.append(s)
                s = parent[s]
    
            path.append(source)
            path.reverse()

    
            max_flow += path_flow
    
            v = sink
            while v != source:
                u = parent[v]
                self.adj[u][v] -= path_flow
                self.adj[v][u] += path_flow
                self.flow[u][v] += path_flow
                v = parent[v]
    
            residual_graph = Graph(self.V)
            for u in range(self.V):
                for v in range(self.V):
                    residual_graph.add_edge(u, v, self.lower_bound[u][v], self.adj[u][v])
            residual_graphs.append(residual_graph)
    
        return max_flow,  residual_graphs

    def get_flows(self):
        return self.flow

    def get_residual_graph(self):
        residual_graph = Graph(self.V)

        for u in range(self.V):
            for v in range(self.V):
                residual_graph.add_edge(u, v, self.lower_bound[u][v], self.adj[u][v])

        return residual_graph
    
# Create a graph given in the example
g = Graph(15)
#initial layer
g.add_edge(0, 1, 7, 13)
g.add_edge(0, 2, 5, 3)
g.add_edge(0, 3, 6, 9)
g.add_edge(0, 4, 5, 12)


#intermediate layer
g.add_edge(1, 2, 1, 5)
g.add_edge(1, 5, 2, 14)
g.add_edge(1, 6, 2, 16)
g.add_edge(1, 7, 2, 10)

g.add_edge(2, 6, 3, 11)
g.add_edge(2, 8, 2, 8)

g.add_edge(3, 6, 3, 12)
g.add_edge(3, 8, 3, 18)

g.add_edge(4, 3, 1, 10)
g.add_edge(4, 8, 2, 20)
g.add_edge(4, 9, 3, 13)



g.add_edge(5, 10, 4, 8)

g.add_edge(6, 7, 1, 6)
g.add_edge(6, 10, 3, 15)
g.add_edge(6, 11, 2, 12)
g.add_edge(6, 12, 4, 20)

g.add_edge(7, 10, 1, 8)
g.add_edge(7, 13, 2, 18)



#final layer
g.add_edge(8, 12, 1, 10)
g.add_edge(9, 12, 3, 15)
g.add_edge(10, 14, 9, 1)
g.add_edge(11, 10, 1, 3)
g.add_edge(11, 12, 2, 10)
g.add_edge(11, 14, 2, 18)
g.add_edge(12, 14, 10, 9)
g.add_edge(13, 14, 2, 10)



source = 0
sink = 14    

max_flows_matrix = g.get_flows()
max_flow, residual_graphs = g.edmonds_karp(source, sink)
print(f"The maximum possible flow is {max_flow}")
print("Maximum Flow Matrix:")
for row in max_flows_matrix:
    print(row)



print("Residual Graphs:")
for i, residual_graph in enumerate(residual_graphs):
    print(f"Iteration {i+1}:")
    residual_adjacency = residual_graph.adj
    for row in residual_adjacency:
        print(row)