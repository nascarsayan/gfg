def getMinSteps(arr, n):
  inf = float('inf')
  minArr = [inf] * n
  minArr[0] = 0
  for cStep in range(1, n):
    for prev in range(cStep):
      if minArr[prev] < inf and prev + arr[prev] >= cStep and minArr[prev] < minArr[cStep] - 1:
        minArr[cStep] = minArr[prev] + 1
  if minArr[n - 1] < inf:
    return minArr[n - 1]
  return -1


t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(getMinSteps(arr, n))
