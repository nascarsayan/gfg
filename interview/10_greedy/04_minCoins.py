DENOM = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def getChange(mon):
  idx = -1
  change = []
  while mon > 0:
    cnotes = mon // DENOM[idx]
    change.extend([DENOM[idx]] * cnotes)
    mon = mon % DENOM[idx]
    idx -= 1
  return change


t = int(input())
for i in range(t):
  mon = int(input())
  print(' '.join(list(map(str, getChange(mon)))))
