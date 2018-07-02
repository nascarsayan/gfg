def getMaxAct(act, n):
  cnt = 1
  curr = 0
  time = act[curr][1]
  while curr < n and time < act[-1][1]:
    while curr < n and act[curr][0] < time:
      curr += 1
    if curr != n:
      cnt += 1
      time = act[curr][1]
  return cnt


t = int(input())
for i in range(t):
  n = int(input())
  start = list(map(int, input().strip().split()))
  end = list(map(int, input().strip().split()))
  act = sorted([(start[i], end[i]) for i in range(n)], key=lambda x: x[1])
  print(getMaxAct(act, n))
