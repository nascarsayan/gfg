from collections import defaultdict


class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices
    for v in range(vertices):
      self.graph[v] = []

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def findRootParent(self, parent, v):
    if parent[v] == -1:
      return v
    else:
      return self.findRootParent(parent, parent[v])

  def union(self, parent, u, v):
    pu = self.findRootParent(parent, u)
    pv = self.findRootParent(parent, v)
    parent[pu] = pv

  def isCyclic(self):
    parent = [-1] * self.V
    for u in self.graph:
      for v in self.graph[u]:
        pu = self.findRootParent(parent, u)
        pv = self.findRootParent(parent, v)
        if pu == pv:
          return True
        self.union(parent, u, v)
    return False


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
  print("Graph contains cycle")
else:
  print("Graph does not contain cycle ")
