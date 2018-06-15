def getLongPal(inp):
  l = len(inp)
  dpPal = [[False] * lr for lr in range(l, 0, -1)]
  # l = 1
  for idx in range(l - 1, -1, -1):
    dpPal[idx][0] = True
  st = 0
  sz = 1
  # l = 2
  for idx in range(l - 2, -1, -1):
    if inp[idx] == inp[idx + 1]:
      dpPal[idx][1] = True
      st = idx
      sz = 2
  # l > 2
  for k in range(3, l + 1):
    for idx in range(l - k, -1, -1):
      if dpPal[idx + 1][k - 3] and inp[idx] == inp[idx + k - 1]:
        dpPal[idx][k - 1] = True
        st = idx
        sz = k
  return inp[st : st + sz]

t = int(input())
for et in range(t):
  inp = input()
  print(getLongPal(inp))
