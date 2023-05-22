from collections import defaultdict
 

def adicionaAresta(grafo,u,v, cap):
    grafo[u].append([v, cap])


    
def imprime(grafo):
    print(grafo)

# Busca em largura      
def BFS(n, grafo, s, t, parent):
    visitados = [False] * n
 
    fila = []
    fila.append(s)
    visitados[s] = True
 
    while fila:
        u = fila.pop(0)
 
        for v in grafo[u]:
            if visitados[v[0]] == False and v[1]>0:
                fila.append(v[0])
                visitados[v[0]] = True
                parent[v[0]] = u
                if v[0] == t:
                    print(parent)
                    return True
    return False

def FordFulkerson(graph, source, sink, n):
 
        # Este array é preenchido pela procura BFS e guarda o caminho de aumento
        parent = [-1]*n      # pais
 

        max_flow = 0 # There is no flow initially

        while BFS(n, graph, source, sink, parent) :
            # determinar o mínimo das capacidades do caminho
            path_flow = float('inf')
            s = sink

            while ( s != source ):
                for v in graph[ parent[s] ]:
                    if v[0] == s:
                        path_flow = min( path_flow, v[1] )
                        break
                s = parent[s]      

            # a atualizar o fluxo máximo
            max_flow = max_flow + path_flow 

            # atualizar as capacidades residuais
            v = sink 
            while ( v != source ):
                u = parent[v]
                for no in graph[u]:
                    if no[0] == v:
                        no[1] = no[1] - path_flow
                        break
                for no in graph[v]:
                    if no[0] == u:
                        no[1] = no[1] + path_flow   
                        break
                v = parent[v]

        return max_flow

grafo = defaultdict(list)
n=6      # numero de vertices 
adicionaAresta(grafo, 0, 1, 16)
adicionaAresta(grafo, 0, 2, 13)
adicionaAresta(grafo, 1, 2, 10)
adicionaAresta(grafo, 1, 3, 12)
adicionaAresta(grafo, 2, 1, 4)
adicionaAresta(grafo, 2, 4, 14)
adicionaAresta(grafo, 3, 2, 9)
adicionaAresta(grafo, 3, 5, 20)
adicionaAresta(grafo, 4, 3, 7)
adicionaAresta(grafo, 4, 5, 4)

# Para o grafo residual - e' necessario inserir as arestas contrarias com capaciddade 0
adicionaAresta(grafo, 1, 0, 0)
adicionaAresta(grafo, 2, 0, 0)
adicionaAresta(grafo, 3, 1, 0)
adicionaAresta(grafo, 4, 2, 0)
adicionaAresta(grafo, 2, 3, 0)
adicionaAresta(grafo, 5, 3, 0)
adicionaAresta(grafo, 3, 4, 0)
adicionaAresta(grafo, 5, 4, 0)

from pprint import pprint
pprint(grafo)

print(f'Fluxo maximo = {FordFulkerson(grafo, 0, 5, n)}')


import networkx


