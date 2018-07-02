def getMaxLen(arr, n):
  sarr = sorted(arr)
  l = 1
  ml = l
  for i in range(1, n):
    if sarr[i] - sarr[i - 1] > 1:
      ml = max(ml, l)
      l = 1
    elif sarr[i] - sarr[i - 1] == 1:
      l += 1
  ml = max(ml, l)
  return ml


def getMaxLenHash(arr, n):
  ml = 1
  for idx in range(n):
    if arr[idx] - 1 not in arr:
      l = 1
      v = arr[idx] + 1
      while v in arr:
        l += 1
        v += 1
      ml = max(ml, l)
  return ml


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(getMaxLenHash(arr, n))
