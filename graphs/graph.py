from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def BFS(self, s):
    visited = [False] * (len(self.graph))
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:
      curr = queue.pop(0)
      print(curr, end=' ')

      for adj in self.graph[curr]:
        if not visited[adj]:
          queue.append(adj)
          visited[adj] = True
    print()

  def DFSUtil(self, vertex, visited):
    visited[vertex] = True
    print(vertex, end = ' ')
    for adj in self.graph[vertex]:
      if not visited[adj]:
        self.DFSUtil(adj, visited)

  def DFS(self, s):
    visited = [False] * (len(self.graph))
    self.DFSUtil(s, visited)
    print()

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

def BFSdriver():
  print ('Following is Breadth First Traversal (starting from vertex 2)')
  g.BFS(2)

def DFSdriver():
  print ('Following is Depth First Traversal (starting from vertex 2)')
  g.DFS(2)

DFSdriver()