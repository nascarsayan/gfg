def remAdjDup(inp):
  if len(inp) == 0:
    return inp
  last = inp[0]
  filInp = inp[0]
  delIt = False
  for c in inp[1:]:
    if c == last:
      delIt = True
    else:
      if delIt:
        filInp = filInp[:-1]
        delIt = False
      filInp += c
    last = c
  if delIt:
    filInp = filInp[:-1]
  if inp == filInp:
    return inp
  else:
    return remAdjDup(filInp)

t = int(input())
for et in range(t):
  inp = input()
  print(remAdjDup(inp))
