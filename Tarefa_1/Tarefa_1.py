from collections import deque
import time
start = time.time()

def merge_sort(arr):
    n = len(arr)
    if ( n == 1):
        return arr
    
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    return merge(merge_sort(left), merge_sort(right))

def merge(l, r):
    m = len(l) + len(r)
    s = []
    l.append([0,float('inf')])
    r.append([0,float('inf')])
    i = j = 0
    for k in range(m):
        if l[i][1] < r[j][1]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    return s

def merge_dic(dicionario):
    arr = []
    for i in range(len(dicionario)):
        arr.append([dicionario[i],len(dicionario[i])])
    
    arr = merge_sort(arr)
    return arr
        
def binary_search_1(vector, number, mid, start_index=0): ## binary search para o index do numero que temos
    if len(vector) == 1:
        if vector[0][1] == number:
            return start_index
        else:
            return False
        
    new_mid = len(vector) // 2
    left = vector[:new_mid]
    right = vector[new_mid:]

    if left[len(left)-1][1] >= number:
        mid -= 1
        return binary_search_1(left, number, mid, start_index)
        
    else:
        if right[0][1] <= number:
            mid += 1
            return binary_search_1(right, number, mid, start_index + new_mid)
        else:
            return False
        
def binary_search_2(vector, number, mid, start_index=0): ## binary search para o index do numero a frente
    if len(vector) == 1:
        if vector[0][1] > number:
            return start_index
        else:
            return False
        
    new_mid = len(vector) // 2
    left = vector[:new_mid]
    right = vector[new_mid:]

    if left[len(left)-1][1] > number:
        mid -= 1
        return binary_search_2(left, number, mid, start_index)
        
    else:
        if right[0][1] <= number:
            mid += 1
            return binary_search_2(right, number, mid, start_index + new_mid)
        else:
            return start_index + new_mid
        
# calcular a distancia entre duas palavras
def word_distance(word1, word2):
    if word1 == word2:
        return 0
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance

def print_distancia_palavras_distantes(array_desj):
    for i in range (len(array_desj)):
        if i == 0 : 
            print ( array_desj[i],len(array_desj)-1)
        else: 
            print(array_desj[i])
        
def print_distancia_palavras_a_um_distancia(palavra_a,palavra_b):
        print ( palavra_a,1)
        print(palavra_b)
        
def print_distancia_palavras_iguais(palavra_a,palavra_b):
        print ( palavra_a,0)
        print(palavra_b)
        
def print_impossivel_chegar(palavra_a,palavra_b):
        print ( palavra_a,-1)
        print(palavra_b)

from collections import deque

def busca_em_largura(words, palavra_a, palavra_b):
    # create a set of all words in the input vector
    if palavra_a not in words or palavra_b not in words:
        return print_impossivel_chegar(palavra_a, palavra_b)
    
    # check if the input words are the same
    if palavra_a == palavra_b:
        return print_distancia_palavras_iguais(palavra_a, palavra_b)
    
    # check if the input words are adjacent
    if word_distance(palavra_a, palavra_b) == 1:
        return print_distancia_palavras_a_um_distancia(palavra_a, palavra_b)

    # use breadth-first search to find the shortest path between the input words
    def find_shortest_path(words, palavra_a, palavra_b):
        queue = deque([(palavra_a,)])
        visited = set([palavra_a])
        
        while queue:
            path = queue.popleft()
            last_word = path[-1]
            if last_word == palavra_b:
                return path
            for word in words:
                if word not in visited and word in words[last_word]:
                    new_path = path + (word,)
                    queue.append(new_path)
                    visited.add(word)
        
        return None
    
    # find the shortest path between the input words using breadth-first search
    path = find_shortest_path(words, palavra_a, palavra_b)
    
    # print the results
    if path:
        print_distancia_palavras_distantes(path)
    else:
        print_impossivel_chegar(palavra_a, palavra_b)


# def calcular_distancias_dicionario(words):
#     dicionario_dist = {}

#     for word1 in words:
#         dicionario_dist[word1[0]]=[]
#         for word2 in words:
#             distance = word_distance(word1[0], word2[0])
#             if distance == 1: 
#                 if word2[0] not in dicionario_dist[word1[0]]:
#                     dicionario_dist[word1[0]].append(word2[0])

#     return dicionario_dist

def calcular_distancias_dicionario(words):
    
    start_2 = time.time() 
    dicionario_dist = {}

    for word in words:
        if dicionario_dist.get(word[0]) is None:
            dicionario_dist[word[0]]=[]
        for key in dicionario_dist:
            distance = word_distance(key, word[0])
            if distance == 1:
                dicionario_dist[key].append(word[0])
    
    end_2 = time.time() 
    print('Time :', end_2 - start_2)

    return dicionario_dist

#with open("C:/Users/robuc/Desktop/College/MMAI/1ºYear/2ºSemester/CO/Tarefa_1/dicionario.txt", "r") as file:
with open("/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/dicionario.txt", "r") as file:
    dicionario = file.read()
    words = dicionario.split()
    
dicionario_sorted=merge_dic(words)


palavra_a = 'armas'
palavra_b = 'armas'

idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

dic = calcular_distancias_dicionario(dicionario_sorted[idx_a:idx_b])
#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

palavra_a = 'engenheiro'
palavra_b = 'engenheiro'

idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

palavra_a = 'zebra'
palavra_b = 'citar'


idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

palavra_a = 'caso'
palavra_b = 'casa'

idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

palavra_a = 'casa'
palavra_b = 'cito'

idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

palavra_a = 'os'
palavra_b = 'as'

idx_a = binary_search_1(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)
idx_b = binary_search_2(dicionario_sorted, len(palavra_a),len(dicionario_sorted)//2)

#busca_em_largura(dicionario_sorted[idx_a:idx_b],palavra_a,palavra_b)
busca_em_largura(dic,palavra_a,palavra_b)

end = time.time()
print('Time :', end - start)