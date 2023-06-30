import heapq

def min_cost_max_flow(capacity, cost, source, sink):
    n = len(capacity)
    flow = [[0]*n for _ in range(n)]
    adj = [[i for i, c in enumerate(row) if c > 0] for row in capacity]
 
    def dijkstra():
        dist = [float('inf')]*n
        prev = [None]*n
        found = [False]*n
        dist[source] = 0
        queue = [(0, source)]
        while queue:
            _, u = heapq.heappop(queue)
            if found[u]:
                continue
            found[u] = True
            for v in adj[u]:
                if capacity[u][v] - flow[u][v] > 0:
                    alt = dist[u] + cost[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        heapq.heappush(queue, (alt, v))
        return prev

    total_flow = 0
    total_cost = 0
    while True:
        prev = dijkstra()
        if prev[sink] is None:
            break
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[prev[s]][s] - flow[prev[s]][s])
            s = prev[s]
        total_flow += path_flow
        s = sink
        while s != source:
            flow[prev[s]][s] += path_flow
            flow[s][prev[s]] -= path_flow
            total_cost += path_flow * cost[prev[s]][s]
            s = prev[s]

        # Print residual network
        print("Residual network:")
        for u in range(n):
            for v in adj[u]:
                if capacity[u][v] - flow[u][v] > 0:
                    print(f"{u} -> {v} : {capacity[u][v] - flow[u][v]}")
        print("")

    return total_flow, total_cost

capacities = [
    [0, 13, 6, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 14, 16, 10, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 11, 0, 10, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 12, 0, 20, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 10, 0, 0, 0, 0, 21, 13, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 15, 12, 22, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 18, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 7, 0], 
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

flow, cost = min_cost_max_flow(capacities, costs, 0, 14)

print(flow)
print(cost)