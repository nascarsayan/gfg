def lhssrhsl(arr, n):
  rs = [float('inf')]
  for e in reversed(arr[1:]):
    rs.insert(0, min(rs[0], e))
  lg = arr[0]
  for idx in range(1, len(arr) - 1):
    if arr[idx] > lg and arr[idx] < rs[idx]:
      return arr[idx]
    lg = max(lg, arr[idx])
  return -1


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(lhssrhsl(arr, n))
