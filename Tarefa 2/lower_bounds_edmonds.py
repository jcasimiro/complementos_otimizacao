from collections import defaultdict

# Representação de lista de adjacências de um grafo direcionado
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.flow = [[0 for _ in range(vertices)] for _ in range(vertices)] 
        self.lower_bound = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v,z, w):
        self.adj[u][v] = w  # A capacidade da aresta do nó u para o nó v é w
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
        max_flow = 0  # Não há fluxo inicialmente

        # Aumenta o fluxo enquanto houver um caminho da fonte ao sumidouro
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.adj[parent[s]][s])
                s = parent[s]

            # Adicione o fluxo de caminho ao fluxo geral
            max_flow += path_flow

            # Atualize as capacidades residuais das arestas e arestas reversas ao longo do caminho
            v = sink
            while v != source:
                u = parent[v]
                self.adj[u][v] -= path_flow
                self.adj[v][u] += path_flow
                self.flow[u][v] += path_flow
                v = parent[v]
                
        n = 0
        i = 0
        while i < self.V:
            n += self.lower_bound[0][i]
            i += 1
        
        return max_flow + n
    def get_flows(self):
        max_flows = [[0 for _ in range(self.V)] for _ in range(self.V)]

        for u in range(self.V):
            for v in range(self.V):
                max_flows[u][v] = self.flow[u][v]

        # Adjust the flows based on the lower bounds
        for u in range(self.V):
            for v in range(self.V):
                max_flows[u][v] += self.lower_bound[u][v]

        return max_flows







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

max_flow = g.edmonds_karp(source, sink)
max_flows_matrix = g.get_flows()
print(f"The maximum possible flow is {max_flow}")
print("Maximum Flow Matrix:")
for row in max_flows_matrix:
    print(row)