from collections import deque
import time

#read the dictionary file
def read_dictionary(filename):
    with open(filename, "r") as file:
        dictionary = file.read().split()
    return dictionary 

#convert word into number using prime numbers
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

#calculate each word into a number
def create_prime_dictionary(dictionary):
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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
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
def binary_search(target_word, words, ignored_words):
    # Initialize the left and right pointers
    l, r = 0, len(words) - 1
    # Binary search
    while l <= r:
        m = (l + r) // 2  # Compute the midpoint
        # Check if the word at index m has distance one from the target word
        if is_distance_one(words[m], target_word) and not words[m] in ignored_words:
            return words[m]
        # Update the left or right pointer based on the lexicographical order of the words
        if words[m] < target_word:
            l = m + 1
        else:
            r = m - 1
    # No word with distance one found
    return None

#calculate if words distance is equal to one.
def is_distance_one(word1, word2):
    #compute the absolute difference between the values of the two words
    diff = abs(word1 - word2)
    #check if the absolute difference is equal to the prime factorization of a single letter
    for prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]:
        if diff == prime:
            return True
    return False

#calculate distances in dictionary
def calculate_distances_dictionary(input_word, dictionary):

    distances_dictionary = {}
    distances_dictionary[input_word] = []

    words_calculated = []
    words_not_calculated = []

    words_not_calculated.append(input_word)

    while len(words_not_calculated) > 0:
        word = words_not_calculated[0]
        word_with_distance_one = binary_search(word, dictionary, words_calculated)

        words_calculated.append(word)
        words_not_calculated.remove(word)

        if not word_with_distance_one is None:
            distances_dictionary[input_word].append(word_with_distance_one)
            if not word_with_distance_one in words_calculated:
                words_not_calculated.append(word_with_distance_one)

    if len(distances_dictionary[input_word]) > 0:
        for sub_word in distances_dictionary[input_word]:
            if not sub_word in distances_dictionary:
                sub_distances_dictionary = calculate_distances_dictionary(sub_word, dictionary)
                distances_dictionary.update(sub_distances_dictionary)

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
    dictionary = read_dictionary("/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/mini_dic.txt")
    #convert words into numbers
    prime_dictionary = create_prime_dictionary(dictionary)
    #get dictionary only with numbers
    prime_numbers_dictionary = [numbers[1] for numbers in prime_dictionary]
    #read input file
    input_words = read_input("/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/input_01.txt")
    #output filename
    output_filename = "/Users/josecasimiro/Projects/Isel/complementos_otimizacao/Tarefa_1/ficheiros_teste/output_tarefa_01.txt"
    #sort the dictionary content by length and words
    prime_dictionary_sorted = merge_sort(prime_numbers_dictionary)
    #save the output to a text variable
    output_txt = ""
    #iterate through input values
    for pair in input_words:
        word_start = word_to_number(pair[0])
        word_end = word_to_number(pair[1])

        if not word_start in prime_numbers_dictionary or not word_end in prime_numbers_dictionary:
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

        #calculate distances
        distances_dictionary = calculate_distances_dictionary(word_start, prime_dictionary_sorted)
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