def appendDig(num, dig, s, n):
  return num + str(dig), s - dig, n - 1


def getMaxNo(n, s):
  if (s - 9 * n > 0) or (s == 0 and n > 1):
    return -1
  num = ''
  while s >= 9:
    num, s, n = appendDig(num, 9, s, n)
  num, s, n = appendDig(num, s, s, n)
  while n > 0:
    num, s, n = appendDig(num, 0, s, n)
  return num


t = int(input())
for i in range(t):
  n, s = list(map(int, input().strip().split()))
  print(getMaxNo(n, s))
