from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def checkCycleUtil(self, v, visited, path):
    path.append(v)
    visited[v] = True
    for adj in self.graph[v]:
      if visited[adj]:
        if adj in path:
          return False
      else:
        noCycle = self.checkCycleUtil(adj, visited, path)
        if not noCycle:
          return False
    path.pop(v)
    return True

  def checkCycle(self, src):
    visited = [False] * (len(self.graph))
    path = []
    return self.checkCycleUtil(src, visited, path)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

print ('Following is Depth First Traversal (starting from vertex 2) to check for cycle')
print (g.checkCycle(0))
