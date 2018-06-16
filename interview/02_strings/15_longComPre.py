import functools
def longComPre(strArr):
  minL = min(map(lambda s: len(s), strArr))
  if minL == 0:
    return -1
  for idx in range(minL):
    if not functools.reduce(lambda x,y: x and y, map(lambda s: s[idx] == strArr[0][idx], strArr), True):
      if idx == 0:
        return -1
      return strArr[0][:idx]
  return strArr[0][:idx + 1]

n = int(input())
for i in range(n):
  k = int(input())
  strArr = input().strip().split()
  print(longComPre(strArr))
