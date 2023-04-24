import time

#https://www.overleaf.com/project/64468a8ec144b8040e7b1c07

#read the dictionary file
def read_dictionary(filename):
    with open(filename, "r") as file:
        dictionary = file.read().split()
    return dictionary 

#read the input file
def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    inputs = []
    for line in lines:
        values = line.replace("\n", "").split(" ")
        inputs.append([values[0], values[1]])
    return inputs    

#merge sort
def merge_sort(dictionary):
    if len(dictionary) <= 1:
        return dictionary
    mid = len(dictionary) // 2
    left = merge_sort(dictionary[:mid])
    right = merge_sort(dictionary[mid:])
    return merge(left, right)

#merge 
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        elif len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
        else:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result += left[i:]
    result += right[j:]
    return result

#binary search
def binary_search_length(dictionary, length):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        if len(dictionary[mid]) == length:
            start = end = mid
            while start > 0 and len(dictionary[start-1]) == length:
                start -= 1
            while end < len(dictionary)-1 and len(dictionary[end+1]) == length:
                end += 1
            return start, end
        elif len(dictionary[mid]) > length:
            right = mid - 1
        else:
            left = mid + 1

    return None

#calculate if words distance is equal to one.
def is_distance_one(word1, word2):
    distance = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            distance += 1
            if distance > 1:
                return False
    return distance == 1

#calculate distances in dictionary
def calculate_distances_dictionary(dictionary):

    len_dictionary = len(dictionary)

    #initialize distances
    distances_dictionary = []
    for i in range(0, len_dictionary):
        distances_dictionary.append([])

    for i in range(0, len_dictionary):
        word1 = dictionary[i]


        for j in range(i+1, len_dictionary):
            word2 = dictionary[j]

            if is_distance_one(word1, word2):
                distances_dictionary[i].append(j)
                distances_dictionary[j].append(i)

    return distances_dictionary

# use breadth-first search to find the shortest path between the input words

def find_shortest_path( grafo, v_origem, v_destino):
    # cria lista dos vértives visitados (inicializada a False)
    visitado = [False] * len(grafo)
    # cria uma lista que guarda, para cada vértice v, o menor número de arestas entre v_origem e v (inicializada a infinito).
    dist = [float('inf')] * len(grafo)
    # cria uma lista que guarda o caminho mínimo de v_origem a cada vértice v (inicializada a [])
    caminho = [[] for i in range(len(grafo))]
    
    fila = []
    fila.append(v_origem)
    visitado[v_origem] = True
    dist[v_origem] = 0
    caminho[v_origem] = [v_origem]
    
    while fila:
        u = fila.pop(0)
        for v in grafo[u]:
            if visitado[v] == False:
                fila.append(v)
                visitado[v] = True
                dist[v] = dist[u] + 1
                caminho[v] = caminho[u] + [v]
                if v == v_destino:
                    return (dist[v_destino], caminho[v_destino])
    return (-1, [])

#build the output text
def build_output(path, value):
    output_txt = ""
    for i in range(len(path)):
        if i==0:
            output_txt += f"{path[i]} {value}\n"
        else:
            output_txt += f"{path[i]}\n"
    output_txt += "\n"
    return output_txt

#save the result to a file
def save_result(output, filename):
    #save the output to file
    with open(filename, "w") as file:
        file.write(output)
        

def find_index_in_dictionary(word, dictionary):
    index = -1
    for i in range(0, len(dictionary)):
        if word == dictionary[i]:
            index = i
            break
    return index

#main function
def main():
    #save the time the program started
    start_time = time.time()
    #read dictionary file
    dictionary = read_dictionary("/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/dicionario.txt")
    #read input file
    input_words = read_input("/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/input_01.txt")
    #output filename
    output_filename = "/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/output_tarefa_01.txt"
    #sort the dictionary content by length and words
    dictionary_sorted = merge_sort(dictionary)
    #save the output to a text variable
    output_txt = ""
    #iterate through input values
    dictionary_all_distances={}
    for pair in input_words:
        word_start = pair[0]
        word_end = pair[1]

        print(word_start)

        if not word_start in dictionary_sorted or not word_end in dictionary_sorted:
            path = [word_start, word_end]
            output_txt += build_output(path, -1)
            continue
        
        if word_start == word_end:
            path = [word_start, word_end]
            output_txt += build_output(path, 0)
            continue

        if is_distance_one(word_start, word_end):
            path = [word_start, word_end]
            output_txt += build_output(path, 1)
            continue

        #search index start and end for dictionary given a word length
        start_index, end_index = binary_search_length(dictionary_sorted, len(word_start))
        #create a short dictionary
        short_dictionary = dictionary_sorted[start_index:end_index]
        
        if len(word_start) not in dictionary_all_distances:
            distances_dictionary = calculate_distances_dictionary(short_dictionary)
            dictionary_all_distances[len(word_start)] = distances_dictionary
        else:
            distances_dictionary = dictionary_all_distances[len(word_start)]
        
        idx_a =find_index_in_dictionary(word_start, short_dictionary)
        idx_b =find_index_in_dictionary(word_end, short_dictionary)
        path = find_shortest_path(distances_dictionary, idx_a, idx_b)
        path_words=[]

        for i in range (path[0]+1):
            if i ==0:
                path_words.append(short_dictionary[path[1][i]])
            else:
                path_words.append(short_dictionary[path[1][i]])
        #verify if the path as been found
        if path_words:
            output_txt += build_output(path_words, path[0])
        else:
            path_words = [word_start, word_end]
            output_txt += build_output(path_words, -1) 

    #save output to file 
    save_result(output_txt, output_filename)
    #print output on screen
    print(output_txt)
    #save the time the program ended
    end_time = time.time()
    print(f'Elapsed time: {end_time - start_time}')

if __name__ == "__main__":
    main()