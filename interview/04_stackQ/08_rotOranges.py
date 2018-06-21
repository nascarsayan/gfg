class MyE(Exception):
  pass


def isValid(idx, dim):
  return idx[0] >= 0 and idx[0] < dim[0] and idx[1] >= 0 and idx[1] < dim[1]


def allRotten(arr, dim):
  for i in range(dim[0]):
    for j in range(dim[1]):
      if arr[i][j] == 1:
        return False
  return True


def getMinTime(arr, r, c):
  dim = (r, c)
  rotQue = []
  delim = (-1, -1)
  for i in range(r):
    for j in range(c):
      if arr[i][j] == 2:
        rotQue.append((i, j))

  rotQue.append(delim)
  count = 0
  while rotQue:
    while rotQue[0] != delim:
      c = rotQue.pop(0)
      # left
      if isValid((c[0] - 1, c[1]), dim) and arr[c[0] - 1][c[1]] == 1:
        arr[c[0] - 1][c[1]] = 2
        rotQue.append((c[0] - 1, c[1]))
      # right
      if isValid((c[0] + 1, c[1]), dim) and arr[c[0] + 1][c[1]] == 1:
        arr[c[0] + 1][c[1]] = 2
        rotQue.append((c[0] + 1, c[1]))
      # top
      if isValid((c[0], c[1] - 1), dim) and arr[c[0]][c[1] - 1] == 1:
        arr[c[0]][c[1] - 1] = 2
        rotQue.append((c[0], c[1] - 1))
      # bottom
      if isValid((c[0], c[1] + 1), dim) and arr[c[0]][c[1] + 1] == 1:
        arr[c[0]][c[1] + 1] = 2
        rotQue.append((c[0], c[1] + 1))
    rotQue.pop(0)
    if rotQue:
      count += 1
      rotQue.append(delim)
  if not allRotten(arr, dim):
    return -1
  return count


t = int(input())
for i in range(t):
  r, c = map(int, input().strip().split())
  arr = []
  inp = list(map(int, input().strip().split()))
  arr = [inp[i:i + c] for i in range(0, len(inp), c)]
  print(getMinTime(arr, len(arr), len(arr[0])))
