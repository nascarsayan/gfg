def getMinMax(arr, n, k):
  arr.sort()
  chunks = (n + k) // (k + 1)
  minP = sum(arr[:chunks])
  maxP = sum(arr[n - chunks:])
  return minP, maxP


t = int(input())
for _ in range(t):
  n, k = list(map(int, input().strip().split()))
  arr = list(map(int, input().strip().split()))
  print(' '.join(list(map(str, getMinMax(arr, n, k)))))
