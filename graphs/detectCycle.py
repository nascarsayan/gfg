from collections import defaultdict


class Graph():
  def __init__(self, verices):
    self.graph = defaultdict(list)
    self.V = verices

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def isCyclicUtil(self, v, visited, pathStack):
    visited[v] = True
    pathStack[v] = True
    if v not in self.graph.keys():
      return False
    for adj in self.graph[v]:
      if pathStack[adj]:
        return True
      if not visited[adj]:
        if self.isCyclicUtil(adj, visited, pathStack):
          return True
    pathStack[v] = False
    return False

  def isCyclic(self):
    visited = [False] * self.V
    for v in self.graph:
      print(v, visited[v])
      pathStack = [False] * self.V
      if not visited[v]:
        if self.isCyclicUtil(v, visited, pathStack):
          return True
    return False


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 4)
g.addEdge(4, 0)

if g.isCyclic():
  print("Graph has a cycle")
else:
  print("Graph has no cycle")
