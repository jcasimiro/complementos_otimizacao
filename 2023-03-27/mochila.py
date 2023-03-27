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
    l.append([0,0,float('-inf')])
    r.append([0,0,float('-inf')])
    i = j = 0
    for k in range(m):
        if l[i][2] > r[j][2]:
            s.append(l[i])
            i += 1
        else:
            s.append(r[j])
            j += 1
    return s

def problema(peso, valor,cap):
    arr = []
    
    for i in range(len(peso)):
        arr.append([peso[i],valor[i],valor[i]/peso[i]])
    
    print(arr)
    arr = merge_sort(arr)
    valor_m = 0
    i=0
    while(cap >0 and i < len(peso)):
        if(arr[i][0]<=cap):
            valor_m = valor_m + arr[i][1]
            cap = cap - arr[i][0]
        else:
            valor_m = valor_m + arr[i][2]*cap 
            cap = 0
        i += 1
    return (valor_m)


peso = [10, 20, 30, 40, 50]
valor = [20, 30, 66, 40, 60]
cap=100
problema(peso, valor,cap)