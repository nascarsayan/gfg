def strstr(strg, substr):
  pSub = -1
  subPos = 0
  currMat = False
  for idx in range(len(strg)):
    if substr[subPos] == strg[idx]:
      if not currMat:
        currMat = True
        pSub = idx
      subPos += 1
      if subPos == len(substr):
        return pSub
    else:
      currMat = False
      subPos = 0
  return -1

n = int(input())
for i in range(n):
  strg, substr = input().strip().split()
  print(strstr(strg, substr))
