from collections import deque
import copy


def dfs_augmenting_path(capacities, parent, visited, u, sink, path):
    visited[u] = True

    if u == sink:
        return True

    for v in range(len(capacities)):
        if not visited[v] and capacities[u][v] > 0:
            parent[v] = u
            if dfs_augmenting_path(capacities, parent, visited, v, sink, path):
                path.append((u, v))
                return True

    return False

def bellman_ford_max_flow_min_cost(capacities, costs, source, sink):
    num_nodes = len(capacities)
    distance = [float('inf')] * num_nodes
    parent = [-1] * num_nodes
    distance[source] = 0

    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if capacities[u][v] > 0 and distance[u] != float('inf') and distance[u] + costs[u][v] < distance[v]:
                    distance[v] = distance[u] + costs[u][v]
                    parent[v] = u

    # Check for negative cycles
    for u in range(num_nodes):
        for v in range(num_nodes):
            if capacities[u][v] > 0 and distance[u] != float('inf') and distance[u] + costs[u][v] < distance[v]:
                raise ValueError("Graph contains a negative cycle")

    # Calculate the maximum flow and minimum cost
    flow = [[0] * num_nodes for _ in range(num_nodes)]
    total_cost = 0

    while True:
        # Find an augmenting path using DFS
        visited = [False] * num_nodes
        path = []
        found_path = dfs_augmenting_path(capacities, parent, visited, source, sink, path)

        if not found_path:
            break

        # Find the minimum capacity along the augmenting path
        min_capacity = float('inf')
        for u, v in path:
            min_capacity = min(min_capacity, capacities[u][v])

        # Update the flow and costs along the augmenting path
        for u, v in path:
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            total_cost += min_capacity * costs[u][v]

            # Update costs for reverse edges
            costs[v][u] = -costs[u][v]

        # Update capacities for forward and backward edges
        for u, v in path:
            capacities[u][v] -= min_capacity
            capacities[v][u] += min_capacity
            

    return flow, total_cost



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
sink = len(capacities)-1

flow, total_cost = bellman_ford_max_flow_min_cost(capacities, costs, source, sink)
for row in flow:
    print(row)
    
print("Total cost:", total_cost)

print("Total fluxo maximo:", sum(flow[0]))



adicoes = [
    [0,7, 2, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0,0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0,0],
    [0,0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0,0],
    [0,0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0,0],
    [0,0, 0, 1, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0,0],
    [0,0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 2, 2, 0,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,7],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,0],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,8],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,2],
    [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
]


    
print(len(flow))
print(len(adicoes))

def add (max_flows_matrix, adicoes):

    # Checking if the dimensions of the matrices are the same
    if len(max_flows_matrix) != len(adicoes) or len(max_flows_matrix[0]) != len(adicoes[0]):
        print("The matrices must have the same dimensions for addition.")
    else:
        # Creating an empty matrix to store the sum
        sum_matrix = [[0 for _ in range(len(max_flows_matrix[0]))] for _ in range(len(max_flows_matrix))]
    
        # Performing element-wise addition and storing the result in sum_matrix
        for i in range(len(max_flows_matrix)):
            for j in range(len(max_flows_matrix[0])):
                sum_matrix[i][j] = max_flows_matrix[i][j] + adicoes[i][j]
    

    return sum_matrix

sum_matrix = add(flow, adicoes)

print("Total fluxo maximo:", sum(sum_matrix[0]))

for row in sum_matrix:
    print(row)

print("Total cost:", total_cost)

