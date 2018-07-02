def getPairs(arr1, arr2, n1, n2, s):
  pArr = []
  for e1 in sorted(arr1):
    if s - e1 in arr2:
      pArr.append((e1, s - e1))
  return pArr


t = int(input())
for i in range(t):
  n1, n2, s = list(map(int, input().strip().split()))
  arr1 = list(map(int, input().strip().split()))
  arr2 = list(map(int, input().strip().split()))
  pArr = getPairs(arr1, arr2, n1, n2, s)
  if len(pArr) == 0:
    print(-1)
  else:
    print(', '.join(map(lambda x: ' '.join(map(str, x)), pArr)))
