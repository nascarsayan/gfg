def getMeetings(act, n):
  act2 = sorted(act, key=lambda x: x[1])
  curr = 0
  acts = [act2[curr][2] + 1]
  time = act2[curr][1]
  while curr < n and time < act2[-1][1]:
    while curr < n and act2[curr][0] < time:
      curr += 1
    if curr != n:
      acts.append(act2[curr][2] + 1)
      time = act2[curr][1]
  return acts


t = int(input())
for i in range(t):
  n = int(input())
  start = list(map(int, input().strip().split()))
  end = list(map(int, input().strip().split()))
  act = [(start[i], end[i], i) for i in range(n)]
  print(' '.join(list(map(str, getMeetings(act, n)))))
