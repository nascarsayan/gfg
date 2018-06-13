def chocoDist(arr, n, m):
  sArr = sorted(arr)
  minIdx = m - 1
  for idx in range(m, n):
    if (sArr[minIdx] - sArr[minIdx - m + 1] > sArr[idx] - sArr[idx - m + 1]):
      minIdx = idx
  return sArr[minIdx] - sArr[minIdx - m + 1]

t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  m = int(input())
  print(chocoDist(arr, n, m))
