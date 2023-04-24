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
    pai = [] 

    N = 9

    for v in range(N):
        dist.append(float('inf'))
        visitados.append(False)
        lista.append([dist[v], v])
        pai.append(-1)

    lista.remove([dist[s], s])
    dist[s] = 0
    lista.insert(0, [dist[s], s])
    pai[s] = s

    while(lista):
        u = min(lista)
        lista.remove(u)
        visitados[u[1]] = True

        for no in grafo[u[1]]:
            v = no[0]
            d = no[1]
            if visitados[v] == False and dist[u[1]] + d < dist[v]:
                lista.remove([dist[v], v])
                dist[v] = dist[u[1]] + d
                lista.append([dist[v], v])
                pai[v] = u[1]

    return dist, pai

def bellmanFord(grafo, s):
    dist = []
    visitados = []
    pai = [] 

    N = 9

    for v in range(N):
        dist.append(float('inf'))
        visitados.append(False)
        pai.append(-1)

    dist[s] = 0
    pai[s] = s
    for _ in range(N-1):
        for no in grafo:
            for no_v in grafo[no]:
                if dist[no] != float('inf') and dist[no] + no_v[1] < dist[no_v[0]]:
                    dist[no_v[0]] = dist[no] + no_v[1]
                    pai[no_v[0]] = no
    
    for no in grafo:
        for no_v in grafo[no]:
            if dist[no] != float('inf') and dist[no] + no_v[1] < dist[no_v[0]]:
                print('o grafo tem ciclos negativos')

    return dist, pai

dist, pai = dijkstra(grafo, 0)
print(dist)
print(pai)

dist, pai = bellmanFord(grafo, 0)
print(dist)
print(pai)