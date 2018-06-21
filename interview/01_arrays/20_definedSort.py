import bisect


def definedSort(a1, a2, m, n):
  ta1 = sorted([x for x in a1])
  oa1 = []
  visited = [False] * m
  for ea2 in a2:
    idx = bisect.bisect_left(ta1, ea2)
    if ta1[idx] == ea2:
      while (idx < m and ta1[idx] == ea2):
        visited[idx] = True
        oa1.append(ea2)
        idx += 1
  for idx in range(m):
    if not visited[idx]:
      oa1.append(ta1[idx])
  return oa1


t = int(input())
for et in range(t):
  m, n = [int(x) for x in input().split()]
  a1 = [int(x) for x in input().split()]
  a2 = [int(x) for x in input().split()]
  print(' '.join(map(str, definedSort(a1, a2, m, n))))
