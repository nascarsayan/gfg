def maxToys(costArr, n, k):
  t = 0
  while k >= costArr[t]:
    k -= costArr[t]
    t += 1
  return t


t = int(input())
for i in range(t):
  n, k = list(map(int, input().strip().split()))
  costArr = sorted(list(map(int, input().strip().split())))
  print(maxToys(costArr, n, k))
