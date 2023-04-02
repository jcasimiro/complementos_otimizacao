#*************************************************************************************
# ordenar as letras de uma palavra
def merge_sort_word(word):
    if len(word) <= 1:
        return word

    # dividir a palavra em duas metades
    mid = len(word) // 2
    left_half = word[:mid]
    right_half = word[mid:]

    #recursivamente ordenar cada metade
    left_sorted = merge_sort_word(left_half)
    right_sorted = merge_sort_word(right_half)

    #juntar as duas metades ordenadas
    merged = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    merged += left_sorted[i:]
    merged += right_sorted[j:]

    return ''.join(merged)
#*************************************************************************************
# pesquisa binaria
def binary_search(word, letter):
    
    if len(word)==1:
        if word[0]==letter:
            return True
        else:
            return False
        
    mid = len(word) // 2
    left = word[:mid]
    right = word[mid:]

    if left[len(left)-1] >= letter:
        return binary_search(left, letter)
    else:
        if right[0] <= letter:
            return binary_search(right, letter)
        else:
            return False