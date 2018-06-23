from collections import defaultdict


def isRearrangeable(inp):
  cnt = defaultdict(int)
  for c in inp:
    cnt[c] += 1
  l = len(inp)
  for k in cnt.keys():
    if cnt[k] > (l + 1) // 2:
      return 0
  return 1


t = int(input())
for i in range(t):
  inp = input()
  print(isRearrangeable(inp))
