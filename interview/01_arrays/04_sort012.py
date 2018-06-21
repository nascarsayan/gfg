def sort012(arr, n):
  n0 = 0
  n1 = 0
  for earr in arr:
    if earr == 0:
      n0 += 1
    elif earr == 1:
      n1 += 1
  print(' '.join(['0'] * n0 + ['1'] * n1 + ['2'] * (n - n0 - n1)))


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  sort012(arr, n)
