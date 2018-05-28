def kanade(arr):
  maxFin = 0
  maxCurr = 0
  for earr in arr:
    maxCurr += earr
    if maxCurr > maxFin:
      maxFin = maxCurr
    if maxCurr < 0:
      maxCurr = 0
  if maxFin == 0:
    maxFin = arr[0]
    for earr in arr:
      if maxFin < earr:
        maxFin = earr
  return maxFin

t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(kanade(arr))