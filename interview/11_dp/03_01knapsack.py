def getMax(vArr, wArr, n, w):
  dpArr = [[0 for _ in range(n + 1)] for _ in range(w + 1)]
  for cw in range(1, w + 1):
    for ci in range(1, n + 1):
      dpArr[cw][ci] = dpArr[cw][ci - 1]
      if cw >= wArr[ci - 1]:
        dpArr[cw][ci] = max(dpArr[cw - wArr[ci - 1]][ci - 1] + vArr[ci - 1],
                            dpArr[cw][ci - 1])
  return dpArr[w][n]


t = int(input())
for _ in range(t):
  n = int(input())
  w = int(input())
  vArr = list(map(int, input().strip().split()))
  wArr = list(map(int, input().strip().split()))
  print(getMax(vArr, wArr, n, w))
