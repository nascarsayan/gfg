def findSingle(arr, n):
  l = 0
  r = n - 1
  if n == 1:
    return arr[0]
  while (l <= r):
    m = (l + r) // 2
    if m % 2 == 0:
      if m < n - 1 and arr[m] == arr[m + 1]:
        l = m + 2
      elif m == 0 or arr[m] != arr[m - 1]:
        return arr[m]
      else:
        r = m - 2
    else:
      if m > 0 and arr[m] == arr[m - 1]:
        l = m + 1
      elif m == n - 1 or arr[m] != arr[m + 1]:
        return arr[m]
      else:
        r = m - 1
  return arr[0]


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(findSingle(arr, n))
