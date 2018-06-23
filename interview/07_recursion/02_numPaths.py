def numPaths(r, c):
  nP = [1] * c
  for _ in range(r - 1):
    for j in range(1, c):
      nP[j] = nP[j] + nP[j - 1]
  return nP[c - 1]


t = int(input())
for i in range(t):
  r, c = list(map(int, input().strip().split()))
  print(numPaths(r, c))
