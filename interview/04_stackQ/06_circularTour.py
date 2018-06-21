def tour(lis, n):
  savings = list(map(lambda x: x[0] - x[1], lis))
  st = 0
  fl = 1
  cost = savings[0]
  while True:
    while cost < 0 and st < fl and st < n:
      cost -= savings[st]
      st += 1
    if st == n:
      return -1
    while cost >= 0 and fl - st < n:
      cost += savings[fl % n]
      fl += 1
    if fl - st == n and cost > 0:
      return st
  return -1


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  lis = []
  for i in range(1, 2 * n, 2):
    lis.append([arr[i - 1], arr[i]])
  print(tour(lis, n))
