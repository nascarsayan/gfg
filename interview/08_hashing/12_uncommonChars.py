from collections import defaultdict


def uncommonChar(s1, s2):
  pre = defaultdict(int)
  for es1 in s1:
    pre[es1] = 1
  for es2 in s2:
    if pre[es2] == 1:
      pre[es2] = -1
    elif pre[es2] > -1:
      pre[es2] = 2
  ret = ''
  for c in sorted(pre.keys()):
    if pre[c] > 0:
      ret += c
  return ret

t = int(input())
for i in range(t):
  s1 = input()
  s2 = input()
  print(uncommonChar(s1, s2))