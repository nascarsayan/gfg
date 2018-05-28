def equilibrium(arr, n):
  s = sum(arr)
  ls = - arr[-1]
  rs = s
  ind = 0
  for ind in range(n):
    ls += arr[ind - 1]
    rs -= arr[ind]
    if ls == rs:
      break
  if ls == rs:
    return ind + 1
  else:
    return -1

t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(equilibrium(arr, n))