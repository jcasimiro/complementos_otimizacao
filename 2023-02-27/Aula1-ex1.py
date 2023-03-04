
file = open("2023-02-27/grafo.txt", "r")
n = int(file.readline())
n_arestas = int(file.readline())
m_adj = [[0 for i in range(n+1)] for j in range(n+1)]
visitado = [0 for i in range(n+1)]
for i in range(0, n_arestas):
    lista = file.readline().split(" ")
    a = int(lista[0])
    b = int(lista[1])
    m_adj[a][b]=1
    m_adj[b][a]=1

def imprime_matriz(m_adj):
    for linha in m_adj:
        print (linha)

def dfs(v):
    visitado[v]=1 
    for i in range(1, n+1):
        if m_adj[v][i] == 1 and visitado[i] == 0:
            print(v, "-»", i)
            dfs(i)

imprime_matriz(m_adj)
dfs(1)