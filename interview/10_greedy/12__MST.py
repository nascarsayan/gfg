def spanningTree(graph, n, e):
  edges = []
  for i in range(n):
    for j in range(n):
      if graph[i][j] > 0:
        edges.append({'w': graph[i][j], 'e': (i, j)})
  edges.sort(key=lambda x: x['w'])
  mst = [False] * n
  mstWt = 0
  print(edges)
  print(e * 2, len(edges))
  for idx in range(e * 2):
    if mst[edges[idx]['e'][0]] and mst[edges[idx]['e'][1]]:
      continue
    mst[edges[idx]['e'][0]] = True
    mst[edges[idx]['e'][1]] = True
    mstWt += edges[idx]['w']
  return mstWt


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n, e = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    matrix = [[0 for i in range(n)] for j in range(n)]
    c = 0
    for j in range(e):
      x = arr[c] - 1
      y = arr[c + 1] - 1
      matrix[x][y] = arr[c + 2]
      matrix[y][x] = arr[c + 2]
      c += 3
    print(spanningTree(matrix, n, e))
