def getMinHeightDiff(arr, n, k):
  if (n < 2):
    return 0
  arr.sort()
  ans = arr[n - 1] - arr[0]
  small = arr[0] + k
  big = arr[n - 1] - k
  if (small > big):
    small, big = big, small
  for idx in range(1, n - 1):
    subtract = arr[idx] - k
    add = arr[idx] + k
    if (subtract >= small or add <= big):
      continue
    if (big - subtract <= add - small):
      small = subtract
    else:
      big = add
  return min(ans, big - small)


t = int(input())
for _ in range(t):
  k = int(input())
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(getMinHeightDiff(arr, n, k))
