
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
    l.append(float('inf'))
    r.append(float('inf'))
    i = j = 0
    for k in range(m):
        if l[i] < r[j]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    return s

def binary_search(vector, number):
    
    if len(vector)==1:
        if vector[0]==number:
            return True
        else:
            return False
        
    mid = len(vector) // 2
    left = vector[:mid]
    right = vector[mid:]

    if left[len(left)-1] >= number:
        return binary_search(left, number)
    else:
        if right[0] <= number:
            return binary_search(right, number)
        else:
            return False
        
        
vector = [2,5,7,6,3,9,4]
ordered_vector = merge_sort(vector)
print(binary_search(ordered_vector, 9))
