from collections import defaultdict

def remDupli(inp):
  out = ''
  cnt = defaultdict(int)
  for c in inp:
    if cnt[c] == 0:
      out += c
      cnt[c] += 1
  return out

t = int(input())
for et in range(t):
  inp = input()
  print(remDupli(inp))
