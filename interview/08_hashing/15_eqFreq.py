from collections import defaultdict


def canEqFreq(s, l):
  cnt = defaultdict(int)
  for earr in s:
    cnt[earr] += 1
  lowFreq = min(cnt.values())
  highFreq = max(cnt.values())
  if highFreq - lowFreq > 1:
    return 0
  if highFreq - lowFreq == 0:
    return 1
  lowFreqCnt = 0
  highFreqCnt = 0
  for k in cnt.keys():
    if cnt[k] == lowFreq:
      lowFreqCnt += 1
    if cnt[k] == highFreq:
      highFreqCnt += 1
  if lowFreq == 1 and lowFreqCnt == 1:
    return 1
  if highFreqCnt == 1:
    return 1
  return 0


t = int(input())
for i in range(t):
  s = input()
  print(canEqFreq(s, len(s)))
