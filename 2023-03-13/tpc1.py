# ------------------------------
# TPC 1 - José Casimiro (A51113)
# ------------------------------

def read_matrix(filename):
    file = open(filename)
    n_linhas = int(file.readline())
    n_colunas = int(file.readline())
    game_matrix = [['' for i in range(n_colunas)] for j in range(n_linhas)]
    for line_index in range(0, n_linhas):
        column = file.readline().split(" ")
        for column_index in range(0, n_colunas):
            game_matrix[line_index][column_index] = column[column_index].replace("\n", "")
    file.close()
    return game_matrix

def main():
    game_matrix = read_matrix("2023-03-13/tabela_tetris.txt")
    

if __name__ == "__main__":
    main()