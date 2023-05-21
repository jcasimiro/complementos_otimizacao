def hungarian_algorithm(cost_matrix):
    n, m = len(cost_matrix), len(cost_matrix[0])
    u = [0]*n
    v = [0]*m
    p = [0]*m
    way = [0]*(m+1)
    
    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        minv = [float('inf')]*m
        used = [False]*(m+1)
        while True:
            used[j0] = True
            i0, delta = p[j0], float('inf')
            for j in range(1, m+1):
                if not used[j]:
                    cur = cost_matrix[i0-1][j-1] - u[i0-1] - v[j-1]
                    if cur < minv[j-1]:
                        minv[j-1], way[j] = cur, j0
                    if minv[j-1] < delta:
                        delta, j1 = minv[j-1], j
            for j in range(j0, m+1):
                if used[j]:
                    u[p[j]-1] += delta
                    v[j-1] -= delta
                else:
                    minv[j-1] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    return -v[0], [(p[j]-1, j-1) for j in range(1, m+1)]

cost_matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
min_cost, pairs = hungarian_algorithm(cost_matrix)
print(f'Minimum cost: {min_cost}')
print(f'Pairs: {pairs}')