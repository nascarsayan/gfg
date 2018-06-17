def getNextLarger(arr, n):
  nextLArr = [arr[-1]]
  out = [-1]
  for idx in range(n - 2, -1, -1):
    while nextLArr and nextLArr[-1] <= arr[idx]:
      nextLArr.pop()
    if len(nextLArr) == 0:
      out.insert(0, -1)
    else:
      out.insert(0, nextLArr[-1])
    nextLArr.append(arr[idx])
  return out

t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().strip().split()]
  print(' '.join(map(str, getNextLarger(arr, n))))
