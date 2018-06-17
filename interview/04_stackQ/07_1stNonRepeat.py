from collections import defaultdict
def nonRep1(arr, n):
  visited = defaultdict(int)
  que = [arr[0]]
  out = [arr[0]]
  visited[arr[0]] += 1
  for c in arr[1:]:
    if visited[c] == 0:
      que.append(c)
      visited[c] += 1
    else:
      if visited[c] == 1:
        que.remove(c)
      visited[c] += 1
    if que:
      out.append(que[0])
    else:
      out.append('-1')
  return out

t = int(input())
for i in range(t):
  n = int(input())
  arr = input().strip().split()
  print(' '.join(nonRep1(arr, n)))
