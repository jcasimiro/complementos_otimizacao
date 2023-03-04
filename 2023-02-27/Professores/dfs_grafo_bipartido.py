# abre o ficheiro
f_in = open("grafo_3.txt" , "r")

# lê o número de vertices
n=int(f_in.readline())

# lê o número de arestas
n_arestas=int(f_in.readline())

# define a matriz de adjacências
m_adj = [[0 for i in range(n+1)] for j in range(n+1)]

# define um array para identifiar os nos visitados
visitado = [0 for i in range(n+1)]

# define um array para identifiar a cor dos nós
cor = [" " for i in range(n+1)]

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

# inicializa variável que identifica se o grafo é bipartido
grafo_bipartido = [True]

# pesquisa em profundidade
def dfs(v):
    visitado[v]=1
    for i in range(1,n+1):
        if (m_adj[v][i]==1 and visitado[i]==0):
            print(v,"(",cor[v],")","->",i)
            if cor[v]=='b':
                cor[i]='p'
            if cor[v]=='p':
                cor[i]='b'
            dfs(i)
        if (m_adj[v][i]==1 and visitado[i]==1 and cor[v]==cor[i]):
            print(v,"(", cor[v] ,")","tem a mesma cor de ",i,"(", cor[i] ,")" )
            grafo_bipartido[0] = False

# principal
cor[1]="b"
dfs(1)
if grafo_bipartido[0]:
    print("O grafo é bipartido")
else:
    print("O grafo não é bipartido")

# fecha o ficheiro
f_in.close()
