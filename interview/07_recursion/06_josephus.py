def josephus(n, k):
  j = 0
  for en in range(2, n + 1):
    j = (j + k) % en
  return j + 1


t = int(input())
for i in range(t):
  n, k = list(map(int, input().strip().split()))
  print(josephus(n, k))
