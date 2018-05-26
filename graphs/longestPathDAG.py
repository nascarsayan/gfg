from collections import defaultdict
# '''
# For the first time, using the adjacency matrix as graph representation
# '''
INF = float('-inf')
class Graph():
  def __init__(self, vertices):
    self.V = vertices
    self.graph = defaultdict(list)
    for v in range(vertices):
      self.graph[v] = []

  def addEdge(self, u, v, w):
    self.graph[u].append((v, w))

  def topoSortUtil(self, v, visited, callStack):
    visited[v] = True
    for adj in self.graph[v]:
      if not visited[adj[0]]:
        self.topoSortUtil(adj[0], visited, callStack)
    callStack.insert(0, v)

  def topoSort(self):
    visited = [False] * self.V
    callStack = []
    for v in self.graph:
      if not visited[v]:
        self.topoSortUtil(v, visited, callStack)
    return callStack

  def longestDistance(self, src):
    topoList = self.topoSort()
    dist = [INF] * self.V
    dist[src] = 0
    for v in topoList:
      if dist[v] is not INF:
        for adj in self.graph[v]:
          if dist[adj[0]] < dist[v] + adj[1]:
            dist[adj[0]] = dist[v] + adj[1]
    print(dist)

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 5, 1)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

s = 1
print('Following are longest distances from source vertex %d' % s)
g.longestDistance(s)