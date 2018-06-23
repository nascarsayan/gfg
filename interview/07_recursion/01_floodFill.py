def floodFill(m, r, c, i, j, oc, nc):
  if i >= r or j >= c or i < 0 or j < 0 or m[i * c + j] != oc:
    return
  m[i * c + j] = nc
  floodFill(m, r, c, i - 1, j, oc, nc)
  floodFill(m, r, c, i + 1, j, oc, nc)
  floodFill(m, r, c, i, j - 1, oc, nc)
  floodFill(m, r, c, i, j + 1, oc, nc)


t = int(input())
for i in range(t):
  r, c = list(map(int, input().strip().split()))
  m = list(map(int, input().strip().split()))
  i, j, nc = list(map(int, input().strip().split()))
  floodFill(m, r, c, i, j, m[i * c + j], nc)
  print(' '.join(map(str, m)))
