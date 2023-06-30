from collections import deque
from heapq import heappop, heappush

def min_cost_max_flow(capacities, costs, source, sink):
    n = len(capacities)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(n):
            #if capacities[u][v] or capacities[v][u]: adj[u].add(v); adj[v].add(u)
            if capacities[u][v]: adj[u].add(v)
    flows = [[0]*n for _ in range(n)]
    min_cost = 0

    while True:
        parent = [-1]*n
        dist = [float('inf')]*n
        dist[source] = 0
        pq = [(0, source)]
        while pq:
            d, u = heappop(pq)
            if d != dist[u]: continue
            for v in adj[u]:
                new_dist = dist[u] + costs[u][v] - costs[v][u]
                if capacities[u][v] - flows[u][v] > 0 and dist[v] > new_dist:
                    dist[v] = new_dist
                    parent[v] = u
                    heappush(pq, (new_dist, v))

        if parent[sink] == -1: break
        path = []
        v = sink
        while v != -1: path.append(v); v = parent[v]
        path = path[::-1]
        flow = min(capacities[u][v] - flows[u][v] for u, v in zip(path, path[1:]))
        for u, v in zip(path, path[1:]):
            min_cost += flow * costs[u][v]
            flows[u][v] += flow
            flows[v][u] -= flow
            print(str(u) + "-> (" + str(flow) + ") ->" + str(v))
        print("")

    return min_cost, flows

# Your inputs here
capacities = [
    [0, 13, 6, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 14, 16, 10, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 11, 0, 10, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 12, 0, 20, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 10, 0, 0, 0, 0, 21, 13, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 15, 12, 22, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 18, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 11, 0, 20], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



costs = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
] 

source = 0
sink = len(capacities) - 1

min_cost, flows = min_cost_max_flow(capacities, costs, source, sink)

print("Min cost:", min_cost)
print("Max flow:", sum(flows[source]))
