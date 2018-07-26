def minCoinsRem(arr, n, k):
  minSum = float('inf')
  csum = 0
  st = 0
  remSt = 0
  while remSt < n and arr[remSt] - arr[st] <= k:
    remSt += 1
  for idx in range(remSt, n):
    csum += arr[idx] - arr[st] - k
  minSum = min(minSum, csum)
  while remSt < n and st < n - 1:
    csum += arr[st]
    while remSt < n and arr[remSt] - arr[st + 1] <= k:
      csum -= arr[remSt] - arr[st] - k
      remSt += 1
    csum -= (n - remSt) * (arr[st + 1] - arr[st])
    minSum = min(minSum, csum)
    st += 1
  return minSum


t = int(input())
for i in range(t):
  n, k = list(map(int, input().strip().split()))
  arr = sorted(list(map(int, input().strip().split())))
  print(minCoinsRem(arr, n, k))
