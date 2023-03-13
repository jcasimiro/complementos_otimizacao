def merge_sort(vector):
    mid = len(vector) // 2
    
    if len(vector) <= 1:
        return vector
    
    left_half = merge_sort(vector[:mid])
    right_half = merge_sort(vector[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    s = [0 for i in range(len(left)+len(right))]
    i = j = k = 0
    while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1

    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        s[k] = right[j]
        j += 1
        k += 1

    return s

my_list = [4, 2, 7, 1, 3, 6, 5]
my_list = merge_sort(my_list)
print(my_list)