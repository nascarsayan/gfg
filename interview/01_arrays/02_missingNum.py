def missing(arr):
  n = len(arr) + 1
  s = int((n * (n + 1)) / 2)
  for earr in arr:
    s -= earr
  return s


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(missing(arr))
