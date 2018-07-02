from collections import defaultdict


def getNumArr(arr, n):
  currS = defaultdict(int)
  s = 0
  ns = 0
  currS[0] += 1
  for e in arr:
    s += e
    ns += currS[s]
    currS[s] += 1
  return ns


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(getNumArr(arr, n))
