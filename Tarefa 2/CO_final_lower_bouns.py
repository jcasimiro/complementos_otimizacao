from collections import deque
import copy

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.flow = [[0 for _ in range(len(graph))] for _ in range(len(graph))] 



    def bfs(self, source, sink):
        queue = deque()
        visited = set()
        queue.append(source)
        visited.add(source)
        self.graph[source]['parent'] = -1

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if capacity > 0 and v not in visited and v != 'parent':
                    visited.add(v)
                    self.graph[v]['parent'] = u
                    queue.append(v)

                    if v == sink:
                        return True

        return False
    def max_flow(self, source, sink):
        max_flow = 0

        while self.bfs(source, sink):
            path_flow = float('inf')
            
            
            print("\n\n")
            
            
            # Encontra a capacidade mínima ao longo do caminho encontrado pela BFS
            v = sink
            while v != source:
                u = self.graph[v]['parent']
                path_flow = min(path_flow, self.graph[u][v])
                
                
                print(str(v) + "-> (" + str(path_flow) + ") ->" + str(u))
                
                
                v = u

            # Atualiza as capacidades das arestas ao longo do caminho e seus reversos
            v = sink
            while v != source:
                u = self.graph[v]['parent']
                self.graph[u][v] -= path_flow
                self.flow[u][v] += path_flow
                v = u

            max_flow += path_flow

        return max_flow
    
    def get_flows(self):
        return self.flow

# CO Team Code
def remove_lower_bounds(capacities, demands, lower_bounds):
    new_capacities = copy.deepcopy(capacities)
    new_demands = copy.deepcopy(demands)
    new_lower_bounds = copy.deepcopy(lower_bounds)
   

    for i in range(len(lower_bounds)):
        for j in range(len(lower_bounds)):
            if lower_bounds[i][j] > 0:
                lower_bound_value = lower_bounds[i][j]
                
                new_capacities[i][j] -= lower_bound_value
                new_demands[i] += lower_bound_value
                new_demands[j] -= lower_bound_value
                new_lower_bounds[i][j] = 0
    
    return new_capacities, new_demands, new_lower_bounds

def remove_demands(capacities, demands, lower_bounds):
    n = len(capacities) + 2
    new_capacities = [[0]*n for _ in range(n)]
    new_demands = copy.deepcopy(demands)
    new_lower_bounds = copy.deepcopy(lower_bounds)

    #supply
    for i in range(len(demands)):
        if demands[i] < 0: 
           new_capacities[0][i+1] = -1 * demands[i]

    #copy capacities
    for i in range(len(capacities)):
        for j in range(len(capacities)):
            new_capacities[i+1][j+1] = capacities[i][j] 
    
    #demands
    for i in range(len(demands)):
        if demands[i] > 0: 
            new_capacities[i+1][len(new_capacities)-1] = demands[i]   
    
    
    return new_capacities, new_demands, new_lower_bounds 

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



lower_bounds = [
    [0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]





capacities_1, demands_1, lower_bounds_1 = remove_lower_bounds(capacities, demands, lower_bounds)




capacities_2, demands_2, lower_bounds_2 = remove_demands(capacities_1, demands_1, lower_bounds_1)



for row in capacities_2:
    print(row)

# Convertendo a matriz de capacidades em um dicionário de adjacência
graph = {i: {} for i in range(len(capacities_2))}
for u in range(len(capacities_2)):
    for v in range(len(capacities_2[u])):
        graph[u][v] = capacities_2[u][v]

ff = FordFulkerson(graph)
source = 0
sink = len(capacities_2)-1
max_flow = ff.max_flow(source, sink)

print("Fluxo máximo:", max_flow)

max_flows_matrix = ff.get_flows()

for row in max_flows_matrix:
    print(row)
    
    
    
    
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

sum_matrix = add(max_flows_matrix, adicoes)

max_flow = sum(sum_matrix[0])

print("Fluxo máximo:", max_flow)

for row in sum_matrix:
    print(row)
