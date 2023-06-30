from collections import defaultdict

# Representação de lista de adjacências de um grafo direcionado
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.flow = [[0 for _ in range(vertices)] for _ in range(vertices)] 

    def add_edge(self, u, v, w):
        self.adj[u][v] = w  # A capacidade da aresta do nó u para o nó v é w

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
                print(self.adj)
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

        return max_flow
    def get_flows(self):
        return self.flow


# Create a graph given in the example
g = Graph(15)
#camada inicial
g.add_edge(0, 1,  20)
g.add_edge(0, 2,  8)
g.add_edge(0, 3,  15)
g.add_edge(0, 4, 18)


#camada intermédia
g.add_edge(1, 2,  6)
g.add_edge(1, 5,  16)
g.add_edge(1, 6,  18)
g.add_edge(1, 7,  12)

g.add_edge(2, 6,  14)
g.add_edge(2, 8,  10)


g.add_edge(3, 6, 15)
g.add_edge(3, 8,  21)

g.add_edge(4, 3,  11)
g.add_edge(4, 8,  22)
g.add_edge(4, 9,  16)



g.add_edge(5, 10,  12)


g.add_edge(6, 7,  7)
g.add_edge(6, 10,  18)
g.add_edge(6, 11,  14)
g.add_edge(6, 12,  24)



g.add_edge(7, 10,  9)
g.add_edge(7, 13,  20)

#camada final



g.add_edge(8, 12,  11)



g.add_edge(9, 12,  18)

g.add_edge(10, 14,  10)

g.add_edge(11, 10,  4)
g.add_edge(11, 12, 12)
g.add_edge(11, 14, 20)



g.add_edge(12, 14,19)


g.add_edge(13, 14, 12)


source = 0
sink = 14

max_flow = g.edmonds_karp(source, sink)
max_flows_matrix = g.get_flows()
print(f"The maximum possible flow is {max_flow}")
print("Maximum Flow Matrix:")
for row in max_flows_matrix:
    print(row)