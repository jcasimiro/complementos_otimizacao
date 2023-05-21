class HopcroftKarp:
    def __init__(self, graph):
        self.graph = graph
        self.pairs = {}
        self.dist = {}

    def bfs(self):
        queue = []
        for u in self.graph:
            if u not in self.pairs:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')

        self.dist[None] = float('inf')

        while queue:
            u = queue.pop(0)
            if u is not None:
                for v in self.graph[u]:
                    next_u = self.pairs.get(v)
                    if self.dist[next_u] == float('inf'):
                        self.dist[next_u] = self.dist[u] + 1
                        queue.append(next_u)

        return self.dist[None] != float('inf')

    def dfs(self, u):
        if u is None:
            return True

        for v in self.graph[u]:
            next_u = self.pairs.get(v)
            if self.dist[next_u] == self.dist[u] + 1 and self.dfs(next_u):
                self.pairs[v] = u
                self.pairs[u] = v
                return True

        self.dist[u] = float('inf')
        return False

    def max_matching(self):
        while self.bfs():
            for u in self.graph:
                if u not in self.pairs:
                    self.dfs(u)
        return len([pair for pair in self.pairs.keys() if pair is not None]) // 2


graph = {
    # nó de partida
    's': ['an'],
    's': ['ba'],
    's': ['ma'],
    's': ['to'],
    's': ['pa'],
    's': ['tu'],
    's': ['zu'],
    # primeira camada
    'an': ['mu'],
    'an': ['pr'],
    'an': ['bu'],
    'an': ['so'],

    'ba': ['mu'],
    'ba': ['vi'],
    'ba': ['fr'],
    'ba': ['sa'],

    'ma': ['vi'],
    'ma': ['fr'],
    'ma': ['pr'],
    'ma': ['sa'],
    'ma': ['bu'],
    'ma': ['so'],

    'to': ['mu'],
    'to': ['pr'],
    'to': ['so'],

    'pa': ['mu'],
    'pa': ['fr'],
    'pa': ['bu'],
    'pa': ['so'],

    'tu': ['vi'],
    'tu': ['pr'],
    'tu': ['sa'],
    'tu': ['so'],

    'zu': ['sa'],
    'zu': ['so'],

    # segunda camada
    'mu': ['t'],
    'vi': ['t'],
    'fr': ['t'],
    'pr': ['t'],
    'sa': ['t'],
    'bu': ['t'],
    'so': ['t']
}
hk = HopcroftKarp(graph)
print(hk.max_matching())