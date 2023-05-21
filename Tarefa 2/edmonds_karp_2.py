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
                v = parent[v]

        return max_flow


# Create a graph given in the example
g = Graph(16)
#camada inicial
g.add_edge(0, 1, 7)
g.add_edge(0, 2, 3)
g.add_edge(0, 3, 4)
g.add_edge(0, 4, 2)
g.add_edge(0, 5, 7)
g.add_edge(0, 6, 2)
g.add_edge(0, 7, 3)

#camada intermédia
g.add_edge(1, 8, 2)
g.add_edge(1, 11, 3)
g.add_edge(1, 13, 2)
g.add_edge(1, 14, 3)

g.add_edge(2, 8, 1)
g.add_edge(2, 9, 2)
g.add_edge(2, 10, 2)
g.add_edge(2, 12, 1)

g.add_edge(3, 9, 3)
g.add_edge(3, 10, 1)
g.add_edge(3, 11, 1)
g.add_edge(3, 12, 2)
g.add_edge(3, 13, 1)
g.add_edge(3, 14, 3)

g.add_edge(4, 8, 1)
g.add_edge(4, 11, 1)
g.add_edge(4, 14, 2)

g.add_edge(5, 8, 4)
g.add_edge(5, 10, 2)
g.add_edge(5, 13, 1)
g.add_edge(5, 14, 2)

g.add_edge(6, 9, 1)
g.add_edge(6, 11, 3)
g.add_edge(6, 12, 2)
g.add_edge(6, 13, 1)
g.add_edge(6, 14, 2)

g.add_edge(7, 12, 3)
g.add_edge(7, 14, 1)

#camada final
g.add_edge(8, 15, 3)
g.add_edge(9, 15, 2)
g.add_edge(10, 15, 4)
g.add_edge(11, 15, 3)
g.add_edge(12, 15, 5)
g.add_edge(13, 15, 4)
g.add_edge(14, 15, 4)

source = 0
sink = 15

print(f"The maximum possible flow is {g.edmonds_karp(source, sink)}")