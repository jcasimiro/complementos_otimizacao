# ------------------------------
# TPC 1 - José Casimiro (A51113)
# ------------------------------

output = []

def read_matrix(filename):
    file = open(filename, encoding="utf-8")
    n_linhas = int(file.readline())
    n_colunas = int(file.readline())
    game_matrix = [['' for i in range(n_colunas)] for j in range(n_linhas)]
    for line_index in range(0, n_linhas):
        column = file.readline().split(" ")
        for column_index in range(0, n_colunas):
            game_matrix[line_index][column_index] = column[column_index].replace("\n", "")
    file.close()
    return game_matrix

def dfs(matriz, x, y, visitas, depth):
    # se já foi visitado sair
    if visitas[x][y] == 1:
        return
    # marcar como visitado
    visitas[x][y] = 1
    # variáveis auxiliares da dimensão da matriz
    max_x = len(matriz)
    max_y = len(matriz[0])
    # mostra a coordenadas para depuração (pode ser comentado)
    #print (str(x) + "," + str(y) + "," + matriz[x][y] + "," + str(depth), "," + str(visitas[x][y]))
    # se a posição corrente conter um cardinal
    if matriz[x][y] == "#":
        if depth == 0:
            output.append(1)
        else:
            output[len(output)-1] += 1
        depth += 1
        if y < max_y-1:
            dfs(matriz, x, y+1, visitas, depth)
        if y > 0:
            dfs(matriz, x, y-1, visitas, depth)
        if x < max_x-1:
            dfs(matriz, x+1, y, visitas, depth)
        if x > 0:
            dfs(matriz, x-1, y, visitas, depth)

    # continuar a pesquisar a matriz
    if depth == 0:
        for vx in range(max_x):
            for vy in range(max_y):
                if visitas[vx][vy] == 0:
                    dfs(matriz, vx, vy, visitas, 0)

def main():
    game_matrix = read_matrix("2023-03-13/tabela_tetris.txt")
    visitas_matriz = [[0 for i in range(len(game_matrix[0]))] for j in range(len(game_matrix))]
    dfs(game_matrix, 0, 0, visitas_matriz, 0)
    print("Número de peças: " + str(len(output)))
    print("Maior peça: " + str(max(output)))
    print(output)
    #write file

if __name__ == "__main__":
    main()