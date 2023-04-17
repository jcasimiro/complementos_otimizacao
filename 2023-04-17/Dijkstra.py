# import numpy as np
# grafo = [1,2,3,4,5]
# c=[[1,2,3],[1,3,2],[2,3,2],[3,4,1],[4,5,2]]


# a={}
# for i in range(len(grafo)):
#     a[i+1] = []
#     for j in range(len(c)):
#         if c[j][0] == i+1:
#             a[i+1].append([c[j][1],c[j][2]])






# vertice_inicial = '1'

# array_distancias=np.zeros(len(grafo))
# for i in range(len(array_distancias) - 1):
#     array_distancias[i+1]='inf'

# array_final=[vertice_inicial]






########################PROFESSOR#################################3

from collections import defaultdict

grafo = defaultdict(list)

print(grafo)

def adicionar_aresta(grafo,origem,destino,peso):
    novo_no=[destino,peso]
    grafo[origem].append(novo_no)
    return grafo

grafo = adicionar_aresta(grafo, 0, 1, 4)
grafo = adicionar_aresta(grafo, 0, 7, 8)
grafo = adicionar_aresta(grafo, 1, 2, 8)
grafo = adicionar_aresta(grafo, 1, 7, 11)
grafo = adicionar_aresta(grafo, 2, 3, 7)
grafo = adicionar_aresta(grafo, 2, 8, 2)
grafo = adicionar_aresta(grafo, 2, 5, 4)
grafo = adicionar_aresta(grafo, 3, 4, 9)
grafo = adicionar_aresta(grafo, 3, 5, 14)
grafo = adicionar_aresta(grafo, 4, 5, 10)
grafo = adicionar_aresta(grafo, 5, 6, 2)
grafo = adicionar_aresta(grafo, 6, 7, 1)
grafo = adicionar_aresta(grafo, 6, 8, 6)
grafo = adicionar_aresta(grafo, 7, 8, 7)

def dijkstra(grafo, s):
    dist = []
    visitados = []
    lista = []

    N = 8

    for v in range(N):
        dist.append(float('inf'))
        visitados.append(False)
        lista.append([dist[v], v])

    lista.remove([dist[s], s])
    dist[s] = 0
    lista.append([dist[s], s])

    while(lista):
        u = min(lista)
        lista.remove(u)
        visitados[u[1]] = True

        for no in grafo[u[1]]:
            v = no[0]
            d = no[1]
            if visitados[v] == False and dist[u[1]] + d < dist[v]:
                list.remove([dist[v], v])
                dist[v] = dist[u[1]] + d
                lista.append([dist[v], v])
