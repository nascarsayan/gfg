def getMaxHelp(mks, dpa):
  if mks <= 6:
    return
  for ks in range(7, mks + 1):
    dpa[ks - 1] = 0
    for b in range(ks - 3, 0, -1):
      dpa[ks - 1] = max(dpa[ks - 1], (ks - b - 1) * dpa[b - 1])
  return


def getMax(mks, dpa):
  for i in range(min(mks, 6)):
    dpa[i] = i + 1
  getMaxHelp(mks, dpa)


t = int(input())
ks = []
for i in range(t):
  ks.append(int(input()))
  mks = max(ks)
  dpa = [None] * mks
  getMax(mks, dpa)
for e in ks:
  print(dpa[e - 1])
