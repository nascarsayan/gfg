def getMinTime(arr, r, c):
  return r, c

t = int(input())
for i in range(t):
  r, c = map(int, input().strip().split())
  arr = []
  for _ in range(r):
    arr.append(input().strip().split())
  print(getMinTime(arr, r, c))
