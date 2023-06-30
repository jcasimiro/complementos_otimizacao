import networkx as nx
from collections import defaultdict
import networkx as nx

# Use BFS to find if there is a path from source to sink.
def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[sink]

# Function to run Edmonds-Karp algorithm
def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

# Function to add a super source and super sink to the graph.
def add_supers(G, demands, lower_bounds):
    # Adjust the capacities and demands based on the lower bounds.
    total_demand = 0
    for u, v in G.edges():
        if (u, v) in lower_bounds:
            G[u][v]['capacity'] -= lower_bounds[(u, v)]
            demands[u] -= lower_bounds[(u, v)]
            demands[v] += lower_bounds[(u, v)]

    # Create super source (s) and super sink (t).
    nodes = list(G.nodes()) # We create a separate list of nodes to avoid modifying the dictionary while iterating
    for node in nodes:
        if demands[node] > 0:
            G.add_edge('super_source', node, capacity=demands[node])
        elif demands[node] < 0:
            G.add_edge(node, 'super_sink', capacity=-demands[node])
            total_demand += -demands[node]

    return G, total_demand

# Convert the NetworkX graph to adjacency matrix.
def nx_to_adj_matrix(G):
    # Initialize the adjacency matrix.
    adjacency_matrix = [[0 for _ in range(len(G.nodes()))] for _ in range(len(G.nodes()))]
    nodes = list(G.nodes())
    
    for edge in G.edges(data=True):
        u = nodes.index(edge[0])
        v = nodes.index(edge[1])
        adjacency_matrix[u][v] = edge[2]['capacity']

    return adjacency_matrix, nodes

# Function to solve circulation with demands and lower bounds problem
def solve_circulation_with_demands_and_lower_bounds(G, demands, lower_bounds):
    G, total_demand = add_supers(G, demands, lower_bounds)
    adjacency_matrix, nodes = nx_to_adj_matrix(G)
    max_flow = edmonds_karp(adjacency_matrix, nodes.index('super_source'), nodes.index('super_sink'))
    return max_flow == total_demand

# Create a directed graph.
G = nx.DiGraph()

# Add edges and their capacities.
G.add_edge("source", "1", capacity=20)
G.add_edge("source", "2", capacity=8)
G.add_edge("source", "3", capacity=15)
G.add_edge("source", "4", capacity=18)


G.add_edge("1", "2", capacity=6)
G.add_edge("1", "5", capacity=16)
G.add_edge("1", "6", capacity=18)
G.add_edge("1", "7", capacity=12)

G.add_edge("2", "6", capacity=14)
G.add_edge("2", "8", capacity=10)

G.add_edge("3", "6", capacity=15)
G.add_edge("3", "8", capacity=21)
G.add_edge("4", "3", capacity=11)
G.add_edge("4", "8", capacity=22)
G.add_edge("4", "9", capacity=16)

G.add_edge("5", "10", capacity=12)
G.add_edge("6", "7", capacity=7)
G.add_edge("6", "10", capacity=18)
G.add_edge("6", "11", capacity=14)
G.add_edge("6", "12", capacity=24)
G.add_edge("7", "10", capacity=9)
G.add_edge("7", "13", capacity=20)

G.add_edge("8", "12", capacity=11)
G.add_edge("9", "12", capacity=18)
G.add_edge("10", "sink", capacity=10)
G.add_edge("11", "10", capacity=4)
G.add_edge("11", "12", capacity=12)
G.add_edge("11", "sink", capacity=20)
G.add_edge("12", "sink", capacity=19)
G.add_edge("13", "sink", capacity=12)

# Define the demands.
demands = {
    "source": -61, 
    "1": 0, 
    "2": 0, 
    "3": 0, 
    "4": 0, 
    "5": 0, 
    "6": 0, 
    "7": 0, 
    "8": 0, 
    "9": 0, 
    "10": 0, 
    "11": 0, 
    "12": 0, 
    "13": 0, 
    "sink": 61
    }

# Define the lower bounds.
lower_bounds = {
    ("1", "5"): 2, 
    ("1", "5"): 2, 
    ("1", "7"): 2, 
    ("2", "8"): 2,
    ("3", "8"): 3,
    ("3", "6"): 3,
    ("4", "3"): 1,
    ("4", "8"): 2,
    ("4", "9"): 3,
    ("5", "10"): 4,
    ("6", "10"): 3,
    ("6", "11"): 2,
    ("6", "12"): 4,
    ("6", "12"): 4,
    ("7", "10"): 1,
    ("7", "13"): 2,
    ("8", "12"): 1, 
    ("9", "12"): 3, 
    ("B", "sink"): 10
    }

# Check if there's a feasible circulation.
print(solve_circulation_with_demands_and_lower_bounds(G, demands, lower_bounds))  # True or False