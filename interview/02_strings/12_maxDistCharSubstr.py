from collections import defaultdict


def getMaxDistSub(inp):
  visited = defaultdict(lambda: -1)
  visited[inp[0]] = 0
  cLen = 1
  maxLen = 1
  for idx in range(1, len(inp)):
    if visited[inp[idx]] < idx - cLen:
      cLen += 1
    else:
      maxLen = max(maxLen, cLen)
      cLen = idx - visited[inp[idx]]
    visited[inp[idx]] = idx
  maxLen = max(maxLen, cLen)
  return maxLen


t = int(input())
for et in range(t):
  inp = input()
  print(getMaxDistSub(inp))
