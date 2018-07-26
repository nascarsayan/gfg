def isPartitionable(arr, n):
  s = sum(arr)
  if s % 2 != 0:
    return 'NO'
  reqS = s // 2
  pArr = [[False] * (n + 1) for _ in range(reqS + 1)]
  pArr[0] = [True] * (n + 1)
  for csum in range(1, reqS + 1):
    for cele in range(1, n + 1):
      pArr[csum][cele] = pArr[csum][cele - 1]
      if csum >= arr[cele - 1]:
        pArr[csum][cele] = pArr[csum][cele] or pArr[csum - arr[cele - 1]][cele
                                                                          - 1]
  if pArr[reqS][n]:
    return 'YES'
  return 'NO'


t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(isPartitionable(arr, n))
