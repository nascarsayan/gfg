def atoi(inp):
  s = 0
  l = len(inp)
  for idx in range(l):
    asc = ord(inp[l - 1 - idx])
    if asc < 48 or asc > 57:
      if idx == l - 1 and inp[0] == '-':
        return -s
      return -1
    s = int((asc - 48) * (10 ** idx)) + s
  return s

t = int(input())
for i in range(t):
  string = input().strip()
  print(atoi(string))
