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

v = [1,3,6,8,1,4,5,7,9]
print(merge_sort(v))