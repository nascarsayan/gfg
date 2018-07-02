from collections import defaultdict


def minWinLen(s1, s2, l1, l2):
  ret = s1 + s2
  if l1 < l2:
    return '-1'
  cnt = defaultdict(int)
  for es2 in s2:
    cnt[es2] += 1
  st = 0
  fl = 0
  total = l2
  for idx in range(l1):
    if s1[idx] in cnt:
      cnt[s1[idx]] -= 1
      if cnt[s1[idx]] >= 0:
        total -= 1
      if total == 0:
        fl = idx + 1
        while True:
          if s1[st] in cnt:
            if cnt[s1[st]] == 0:
              break
            cnt[s1[st]] += 1
          st += 1
        if fl - st < len(ret):
          ret = s1[st:fl]
  if len(ret) > l1:
    return '-1'
  return ret


t = int(input())
for i in range(t):
  s1 = input()
  s2 = input()
  print(minWinLen(s1, s2, len(s1), len(s2)))
