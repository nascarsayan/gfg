def isSubset(arr1, arr2, n1, n2):
  if n2 > n1:
    return 'No'
  for e2 in arr2:
    if e2 not in arr1:
      return 'No'
  return 'Yes'

t = int(input())
for i in range(t):
  n1, n2 = list(map(int, input().strip().split()))
  arr1 = list(map(int, input().strip().split()))
  arr2 = list(map(int, input().strip().split()))
  print(isSubset(arr1, arr2, n1, n2))