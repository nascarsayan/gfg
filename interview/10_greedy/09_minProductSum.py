def getMinProdSum(arr1, arr2, n):
  arr1.sort()
  arr2.sort(reverse=True)
  s = 0
  for idx in range(n):
    s += arr1[idx] * arr2[idx]
  return s


t = int(input())
for _ in range(t):
  n = int(input())
  arr1 = list(map(int, input().strip().split()))
  arr2 = list(map(int, input().strip().split()))
  print(getMinProdSum(arr1, arr2, n))
