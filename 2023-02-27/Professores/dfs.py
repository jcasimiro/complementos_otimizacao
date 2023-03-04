# abre o ficheiro
f_in = open("grafo_1.txt" , "r")

# lê o número de vertices
n=int(f_in.readline())

# lê o número de arestas
n_arestas=int(f_in.readline())

# define a matriz de adjacências
m_adj = [[0 for i in range(n+1)] for j in range(n+1)]

# define um array para identifiar os nos visitados
visitado = [0 for i in range(n+1)]

# lê as arestas
for i in range(0,n_arestas):
    lista = f_in.readline().split(" ")
    a=int(lista[0])
    b=int(lista[1])    
    m_adj[a][b] = 1
    m_adj[b][a] = 1

# imprime a matriz de adjacências
def imprime_matriz_adj(m_adj):
    for linha in m_adj:
        print(linha)

# pesquisa em profundidade
def dfs(v):
    visitado[v]=1
    for i in range(1,n+1):
        if (m_adj[v][i]==1 and visitado[i]==0):
            print(v,"->",i)
            dfs(i)

# principal
dfs(1)

# fecha o ficheiro
f_in.close()
