def getMinOp(n):
  cnt = 0
  while n > 0:
    if n % 2 == 0 or n == 1:
      cnt += 1
    else:
      cnt += 2
    n = n // 2
  return cnt


t = int(input())
for _ in range(t):
  n = int(input())
  print(getMinOp(n))
