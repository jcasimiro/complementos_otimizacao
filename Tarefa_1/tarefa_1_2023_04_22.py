from collections import deque
import time

def word_to_number(word):
    # Dictionary of prime numbers assigned to each letter of the alphabet
    prime_nums = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
                  'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
                  'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    
    #multiply the prime numbers assigned to each letter to obtain the word's value
    word_value = 1
    for letter in word:
        word_value *= prime_nums[letter.lower()]
        
    return word_value

#read the dictionary file
def read_dictionary(filename):
    with open(filename, "r") as file:
        dictionary = file.read().split()
    prime_dictionary = []
    for word in dictionary:
        prime_dictionary.append([word, word_to_number(word)])
    return prime_dictionary 

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
        if len(left[i][0]) < len(right[j][0]):
            result.append(left[i])
            i += 1
        elif len(left[i][0]) > len(right[j][0]):
            result.append(right[j])
            j += 1
        else:
            if left[i][0] < right[j][0]:
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
    if word1 == word2:
        return False
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
        if ( distance > 1):
            break
    return distance==1

#get all words with distance one from the dictionary for a given word
def get_words_with_distance_one(input_word, dictionary):
    words_distance_1 = []
    for word in dictionary:
        if is_distance_one(input_word, word):
            words_distance_1.append(word)
    return words_distance_1

#calculate distances in dictionary
def calculate_distances_dictionary(input_word, dictionary):

    distances_dictionary = {}

    words_not_calculated = []
    words_calculated = []

    words_not_calculated.append(input_word)

    while len(words_not_calculated) > 0:
        word = words_not_calculated[0]
        words_with_distance_one = get_words_with_distance_one(word, dictionary)
        distances_dictionary[word] = words_with_distance_one

        words_calculated.append(word)
        words_not_calculated.remove(word)

        for word_distance_one in words_with_distance_one:
            if not word_distance_one in words_not_calculated:
                if not word_distance_one in words_calculated:
                        words_not_calculated.append(word_distance_one)

    return distances_dictionary

# use breadth-first search to find the shortest path between the input words
def find_shortest_path(distances_dictionary, word1, word2):
    queue = deque([(word1,)])
    visited = set([word1])
    
    while queue:
        path = queue.popleft()
        last_word = path[-1]
        if last_word == word2:
            return path
        for word in distances_dictionary:
            if word not in visited and word in distances_dictionary[last_word]:
                new_path = path + (word,)
                queue.append(new_path)
                visited.add(word)
    
    return None

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

#main function
def main():
    #save the time the program started
    start_time = time.time()
    #read dictionary file
    dictionary = read_dictionary("/workspaces/complementos_otimizacao/Tarefa_1/ficheiros_teste/dicionario.txt")
    #read input file
    input_words = read_input("/workspaces/complementos_otimizacao/Tarefa_1/ficheiros_teste/input_01.txt")
    #output filename
    output_filename = "/workspaces/complementos_otimizacao/Tarefa_1/ficheiros_teste/output_tarefa_01.txt"
    #sort the dictionary content by length and words
    dictionary_sorted = merge_sort(dictionary)
    #save the output to a text variable
    output_txt = ""
    #iterate through input values
    for pair in input_words:
        word_start = pair[0]
        word_end = pair[1]

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
        #calculate distances
        distances_dictionary = calculate_distances_dictionary(word_start, short_dictionary)
        path = find_shortest_path(distances_dictionary, word_start, word_end)
        #verify if the path as been found
        if path:
            output_txt += build_output(path, len(path)-1)
        else:
            path = [word_start, word_end]
            output_txt += build_output(path, -1) 
    #save output to file 
    save_result(output_txt, output_filename)
    #print output on screen
    print(output_txt)
    #save the time the program ended
    end_time = time.time()
    print(f'Elapsed time: {end_time - start_time}')

if __name__ == "__main__":
    main()