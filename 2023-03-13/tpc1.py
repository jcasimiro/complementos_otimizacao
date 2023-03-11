# ------------------------------
# TPC 1 - José Casimiro (A51113)
# ------------------------------
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

def dfs(matriz, x, y, visitas, max_x, max_y):
    if visitas[x][y] == 1:
        return
    
    visitas[x][y] = 1

    if matriz[x][y] == "#":
        if x > 0:
            dfs(matriz, x-1, y, visitas, max_x, max_y)
        if x < max_x - 1:
            dfs(matriz, x+1, y, visitas, max_x, max_y)
        if y > 0:
            dfs(matriz, x, y-1, visitas, max_x, max_y)
        if y < max_y - 1:
            dfs(matriz, x, y+1, visitas, max_x, max_y)
    else:
        if x < max_x - 1:
            dfs(matriz, x+1, y, visitas, max_x, max_y)
        else:
            if y < max_y - 1:
                dfs(matriz, 0, y+1, visitas, max_x, max_y)

    return 0

def main():
    game_matrix = read_matrix("2023-03-13/tabela_tetris.txt")
    rows_game_matrix = len(game_matrix)
    columns_game_matrix = len(game_matrix[0])
    visitas_matriz = [[0 for i in range(columns_game_matrix)] for j in range(rows_game_matrix)]
    dfs(game_matrix, 0, 0, visitas_matriz, rows_game_matrix, columns_game_matrix)
    #write file

if __name__ == "__main__":
    main()