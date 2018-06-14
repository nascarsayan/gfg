def printPer(inp, visited, perm, l):
  if len(perm) == l:
    print(perm, end=' ')
  for idx in range(l):
    if not visited[idx]:
      visited[idx] = True
      printPer(inp, visited, perm + inp[idx], l)
      visited[idx] = False

def permut(inp):
  l = len(inp)
  visited = [False] * l
  printPer(inp, visited, '', l)
  print()

t = int(input())
for et in range(t):
  inp = input()
  permut(''.join(sorted(inp)))
