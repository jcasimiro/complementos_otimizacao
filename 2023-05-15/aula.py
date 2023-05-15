from collections import defaultdict

grafo = defaultdict(list)

def adicionar_aresta(grafo,origem,destino,peso):
    novo_no=[destino,peso]
    grafo[origem].append(novo_no)
    return grafo

grafo = adicionar_aresta(grafo, 0, 1, 1)
grafo = adicionar_aresta(grafo, 0, 3, 4)
grafo = adicionar_aresta(grafo, 0, 2, 3)
grafo = adicionar_aresta(grafo, 1, 0, 1)
grafo = adicionar_aresta(grafo, 1, 2, 1)
grafo = adicionar_aresta(grafo, 2, 1, 1)
grafo = adicionar_aresta(grafo, 2, 3, 1)

def FloydWarshall(N, grafo):
    dist = [[float('inf') for j in range(N)] for i in range(N)]
    
    for no in grafo:
        for no_viz in grafo[no]:
            dist[no][no_viz[0]] = no_viz[1]
    
    for i in range(N):
        dist[i][i] = 0

    print(dist)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                     dist[i][j] = dist[i][k] + dist[k][j]
        print(dist)

FloydWarshall(4, grafo)