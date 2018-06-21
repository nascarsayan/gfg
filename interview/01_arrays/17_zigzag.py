def zigzag(arr, n):
  sgn = 1
  for idx in range(n - 1):
    if ((arr[idx + 1] - arr[idx]) * sgn < 0):
      arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    sgn *= -1
  return arr


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(' '.join(map(str, zigzag(arr, n))))
