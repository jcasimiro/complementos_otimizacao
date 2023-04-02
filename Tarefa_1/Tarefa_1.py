#*************************************************************************************
# ler ficheiro dicionario
def ler_dicionario(filename):
    lines = []
    dictionary = []

    try:
        file = open(filename, encoding="utf-8")
        lines = file.readlines()
    except IOError:
        print("Erro a ler o ficheiro. Confirme nome e caminho para o ficheiro.")
        return None
    finally:
        if file != None:
            file.close()

    #formatar linhas removendo '\n'
    #adicionar a dimensao de cada palavra
    if not lines is None:
        for line in lines:
            strip_line = line.strip()
            dictionary.append([len(strip_line), strip_line])

    return dictionary
#*************************************************************************************
# ler ficheiro input
def ler_input(filename):
    lines = []
    words_pairs = []

    try:
        file = open(filename, encoding="utf-8")
        lines = file.readlines()
    except IOError:
        print("Erro a ler o ficheiro. Confirme nome e caminho para o ficheiro.")
        return None
    finally:
        if file != None:
            file.close()

    #formatar linhas removendo '\n'
    if not lines is None:
        for line in lines:
            ordered_pairs = line.strip().split(" ")
            if len(ordered_pairs[0]) != len(ordered_pairs[1]):
                raise Exception("Os pares de palavras devem ter obrigatóriamente a mesma dimensão.")
            words_pairs.append(ordered_pairs)

    return words_pairs
#*************************************************************************************
# implementacao do merge sort para uma lista de palavras
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)
#*************************************************************************************
# sub-funcao do merge sort
def merge(left, right):
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        elif left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1           

    result += left[i:]
    result += right[j:]

    return result
#*************************************************************************************
# calcular a distancia entre duas palavras
def word_distance(word1, word2):
    if word1 == word2:
        return 0

    distance = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

#    while(len(word1) > 0):
#        index_word2 = word2.find(word1[0])
#        if index_word2 == -1:
#            distance += 1
#        else:
#            word2 = word2[:index_word2] + word2[index_word2+1:]
#        word1 = word1[:0] + word1[0+1:]

    return distance
#*************************************************************************************
#calcular dicionario para palavra com base na sua dimensao 
def create_dictionary_for_word_len(word, dictionary):
    subdictionary = []

    for entry in dictionary:
        if len(entry[1]) == len(word):
            new_entry = [word_distance(word, entry[1]), entry[1]]
            subdictionary.append(new_entry)

    subdictionary = merge_sort(subdictionary)

    return subdictionary
#*************************************************************************************
#criar grafo a partir da estrutura de dados 
def create_graph(start_word, end_word, dictionary):

    subdictionary = create_dictionary_for_word_len(start_word, dictionary)

    print(start_word)
    if len(subdictionary) > 0:
        for word in subdictionary:
            print(word)

#*************************************************************************************
#função principal 
def main():
    dictionary = ler_dicionario("Tarefa_1/ficheiros_teste/mini_dic.txt")
    input = ler_input("Tarefa_1/ficheiros_teste/input_01.txt")

    for words in input:
        start_word = words[0]
        end_word = words[1]
        create_graph(start_word, end_word, dictionary)
#*************************************************************************************
#entrada programa 
if __name__ == "__main__":
    main()