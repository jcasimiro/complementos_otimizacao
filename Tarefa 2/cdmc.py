def create_residual_graph(capacities):
    num_nodes = len(capacities)
    residual_graph = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            residual_graph[i][j] = capacities[i][j]

    return residual_graph


def find_augmenting_path(residual_graph, source, sink, parent):
    num_nodes = len(residual_graph)
    visited = [False] * num_nodes
    visited[source] = True

    stack = [source]
    while stack:
        u = stack.pop()

        for v in range(num_nodes):
            if not visited[v] and residual_graph[u][v] > 0:
                parent[v] = u
                visited[v] = True
                stack.append(v)
                if v == sink:
                    return True

    return False


def min_cost_circulation_with_demands(capacities, demands, costs):
    num_nodes = len(capacities)
    residual_graph = create_residual_graph(capacities)

    flow = [[0] * num_nodes for _ in range(num_nodes)]
    total_cost = 0

    while True:
        parent = [-1] * num_nodes
        if not find_augmenting_path(residual_graph, 0, num_nodes - 1, parent):
            break

        path_flow = float("inf")
        v = num_nodes - 1

        while v != 0:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        v = num_nodes - 1

        while v != 0:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            #residual_graph[v][u] += path_flow
            flow[u][v] += path_flow
            total_cost += path_flow * costs[u][v]
            v = u

    return flow, total_cost


# Example usage
capacities = [
    [0, 6, 0, 0, 16, 18, 12, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 14, 0, 10, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 15, 0, 21, 0, 0, 0, 0, 0], 
    [0, 0, 11, 0, 0, 0, 0, 22, 16, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 7, 0, 0, 18, 14, 24, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 20], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 12, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

demands = [-20, -8, -15, -18, 0, 0, 0, 0, 0 , 10, 20, 19, 12]

# costs = [
#     [0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 2, 2, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

costs = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

flow, total_cost = min_cost_circulation_with_demands(capacities, demands, costs)

print("Optimal flow values:")
# for i in range(len(flow)):
#     for j in range(len(flow[i])):
#         print(f"Edge ({i+1}, {j+1}): {flow[i][j]}")
for i in range(len(flow)):
    print(flow[i])
print("Total cost:", total_cost)