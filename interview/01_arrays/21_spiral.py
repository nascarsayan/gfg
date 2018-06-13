side = 4
def spiral(arr):
  path = []
  st = 0
  currSz = side
  while(st < currSz):
    for j in range(st, currSz):
      path.append(arr[st][j])
    for i in range(st + 1, currSz):
      path.append(arr[i][currSz - 1])
    for j in reversed(range(st, currSz - 1)):
      path.append(arr[currSz - 1][j])
    for i in reversed(range(st + 1, currSz - 1)):
      path.append(arr[i][st])
    st += 1
    currSz -= 1
  return path

t = int(input())
for et in range(t):
  arr = []
  for r in range(side):
    arr.append([int(x) for x in input().split()])
  print(' '.join(map(str, spiral(arr))))
