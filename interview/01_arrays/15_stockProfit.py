def getTransact(arr, n):
  ts = []
  if n < 2:
    return ts
  i = 0
  while i < n - 1:
    while i < n - 1 and arr[i] >= arr[i + 1]:
      i += 1
    if i == n - 1:
      break
    x = i
    i += 1
    while i < n and arr[i - 1] <= arr[i]:
      i += 1
    ts.append([x, i - 1])
  return ts


def maxProfit(arr, n):
  trans = getTransact(arr, n)
  if len(trans) == 0:
    print('No Profit')
  else:
    for t in trans:
      print('(%d %d)' % (t[0], t[1]), end=' ')
    print('')


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  maxProfit(arr, n)
