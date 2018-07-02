def isPairable(arr, n, k):
  if n % 2 != 0:
    return False
  modEqArr = [0] * k
  for earr in arr:
    modEqArr[earr % k] += 1
  if modEqArr[0] % 2 != 0:
    return False
  if k % 2 == 0 and modEqArr[k // 2] % 2 != 0:
    return False
  for idx in range(1, (k + 1) // 2):
    if modEqArr[idx] != modEqArr[k - idx]:
      return False
  return True


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  k = int(input())
  print(isPairable(arr, n, k))