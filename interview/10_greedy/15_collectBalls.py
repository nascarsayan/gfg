def getMaxBalls(arr1, arr2, n1, n2):
  i1 = 0
  i2 = 0
  cs1 = 0
  cs2 = 0
  ts = 0
  while i1 < n1 and i2 < n2:
    if arr1[i1] == arr2[i2]:
      ts += max(cs1, cs2)
      eq = arr1[i1]
      teq = 0
      while i1 < n1 and arr1[i1] == eq:
        teq += 1
        i1 += 1
      while i2 < n2 and arr2[i2] == eq:
        teq += 1
        i2 += 1
      ts += eq * (teq - 1)
      cs1 = 0
      cs2 = 0
    elif arr1[i1] < arr2[i2]:
      cs1 += arr1[i1]
      i1 += 1
    else:
      cs2 += arr2[i2]
      i2 += 1
  if i1 < n1:
    cs1 += sum(arr1[i1:])
  if i2 < n2:
    cs2 += sum(arr2[i2:])
  ts += max(cs1, cs2)
  return ts


t = int(input())
for _ in range(t):
  n1, n2 = list(map(int, input().strip().split()))
  arr1 = list(map(int, input().strip().split()))
  arr2 = list(map(int, input().strip().split()))
  print(getMaxBalls(arr1, arr2, n1, n2))
