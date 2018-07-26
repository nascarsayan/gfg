def lisLen(arr, n):
  if n == 0:
    return 0
  lisArr = [1] * n
  for curr in range(1, n):
    for pre in range(curr):
      if arr[pre] < arr[curr] and lisArr[pre] >= lisArr[curr]:
        lisArr[curr] = lisArr[pre] + 1
  return max(lisArr)


t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  print(lisLen(arr, n))
