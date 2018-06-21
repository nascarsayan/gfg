from collections import defaultdict


class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices
    for v in range(vertices):
      self.graph[v] = []

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def topoSortUtil(self, v, visited, callStack):
    visited[v] = True
    for adj in self.graph[v]:
      if not visited[adj]:
        self.topoSortUtil(adj, visited, callStack)
    callStack.insert(0, v)

  def topoSort(self):
    visited = [False] * self.V
    callStack = []
    for v in self.graph:
      if not visited[v]:
        self.topoSortUtil(v, visited, callStack)
    print(callStack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topoSort()
