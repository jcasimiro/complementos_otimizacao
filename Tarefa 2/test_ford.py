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
n=15     # numero de vertices 


#camada inicial
adicionaAresta(grafo,0, 1,  20)
adicionaAresta(grafo,0, 2,  8)
adicionaAresta(grafo,0, 3,  15)
adicionaAresta(grafo,0, 4, 18)
adicionaAresta(grafo,1, 0,  0)
adicionaAresta(grafo,2, 0,  0)
adicionaAresta(grafo,3, 0,  0)
adicionaAresta(grafo,4, 0, 0)


#camada intermédia
adicionaAresta(grafo,1, 2,  6)
adicionaAresta(grafo,1, 5,  16)
adicionaAresta(grafo,1, 6,  18)
adicionaAresta(grafo,1, 7,  12)
adicionaAresta(grafo,2, 6,  14)
adicionaAresta(grafo,2, 8,  10)


adicionaAresta(grafo,2, 1,  0)
adicionaAresta(grafo,5, 1,  0)
adicionaAresta(grafo,6, 1,  0)
adicionaAresta(grafo,7, 1,  0)

adicionaAresta(grafo,6, 2,  0)
adicionaAresta(grafo,8, 2,  0)





adicionaAresta(grafo,3, 6, 15)
adicionaAresta(grafo,3, 8,  21)

adicionaAresta(grafo,4, 3,  11)
adicionaAresta(grafo,4, 8,  22)
adicionaAresta(grafo,4, 9,  16)


adicionaAresta(grafo,6, 3, 0)
adicionaAresta(grafo,8, 3,  0)

adicionaAresta(grafo,3, 4,  0)
adicionaAresta(grafo,8, 4,  0)
adicionaAresta(grafo,9, 4,  0)

adicionaAresta(grafo,5, 10,  12)
adicionaAresta(grafo,6, 7,  7)
adicionaAresta(grafo,6, 10,  18)
adicionaAresta(grafo,6, 11,  14)
adicionaAresta(grafo,6, 12,  24)
adicionaAresta(grafo,7, 10,  9)
adicionaAresta(grafo,7, 13,  20)



adicionaAresta(grafo,10, 5,  0)
adicionaAresta(grafo,7, 6,  0)
adicionaAresta(grafo,10, 6,  0)
adicionaAresta(grafo,11, 6,  0)
adicionaAresta(grafo,12, 6,  0)
adicionaAresta(grafo,10, 7,  0)
adicionaAresta(grafo,13, 7,  0)

#camada final


adicionaAresta(grafo,8, 12,  11)
adicionaAresta(grafo,9, 12,  18)
adicionaAresta(grafo,10, 14,  10)
adicionaAresta(grafo,11, 10,  4)
adicionaAresta(grafo,11, 12, 12)
adicionaAresta(grafo,11, 14, 20)
adicionaAresta(grafo,12, 14,19)
adicionaAresta(grafo,13, 14, 12)

adicionaAresta(grafo,12, 8,  0)
adicionaAresta(grafo,12, 9,  0)
adicionaAresta(grafo,14, 10,  0)
adicionaAresta(grafo,10, 11,  0)
adicionaAresta(grafo,12, 11, 0)
adicionaAresta(grafo,14, 11, 0)
adicionaAresta(grafo,14, 12,0)
adicionaAresta(grafo,14, 13, 0)


source = 0
sink = 14

from pprint import pprint
print(grafo)

print(f'Fluxo maximo = {FordFulkerson(grafo, 0, 5, n)}')