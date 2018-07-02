def canBeEqualSum(arr1, arr2, n1, n2):
  s1 = sum(arr1)
  s2 = sum(arr2)
  i1 = 0
  i2 = 0
  while i1 < n1 and i2 < n2:
    ns1 = s1 - arr1[i1] + arr2[i2]
    ns2 = s2 - arr2[i2] + arr1[i1]
    if ns1 == ns2:
      return 1
    if ns1 > ns2:
      i1 += 1
    else:
      i2 += 1
  return -1

t = int(input())
for i in range(t):
  n1, n2 = list(map(int, input().strip().split()))
  arr1 = sorted(list(map(int, input().strip().split())))
  arr2 = sorted(list(map(int, input().strip().split())))
  print(canBeEqualSum(arr1, arr2, n1, n2))
