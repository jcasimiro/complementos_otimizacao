from collections import defaultdict

# Representação de lista de adjacências de um grafo direcionado
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]

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

        # Aumenta o fluxo enquanto houver um caminho da fonte ao destino
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
                v = parent[v]

        return max_flow


# Create a graph given in the example
g = Graph(16)
#camada inicial
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)

g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)

g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)

g.add_edge(3, 5, 20)

g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5

print(f"The maximum possible flow is {g.edmonds_karp(source, sink)}")