file = open("grafo_31.txt", "r")
n = int(file.readline())
n_arestas = int(file.readline())
m_adj = [[0 for i in range(n+1)] for j in range(n+1)]
visitado = [0 for i in range(n+1)]
cor = [0 for i in range(n+1)]

for i in range(0, n_arestas):
    lista = file.readline().split(" ")
    a = int(lista[0])
    b = int(lista[1])
    m_adj[a][b]=1
    m_adj[b][a]=1
    if i == 1:
        cor[i] = 1

def dfs(v):
    visitado[v]=1 
    for i in range(1, n+1):
        if m_adj[v][i] == 1: 
            if visitado[i] == 0:
                if cor[v] == 1:
                    cor[i] = 2
                else:
                    cor[1] = 1  
                dfs(i)
            else:
                if cor[i] == cor[v]:
                    print("Grafo n bipartido")

dfs(1)