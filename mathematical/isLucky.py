def isLucky(n, div):
  while(True):
    if n % div == 0:
      return False
    if n < div:
      return True
    n -= int(n / div)
    div += 1

n = int(input())
if isLucky(n, 2):
  print('%d is lucky' % n)
else:
  print('%d is not lucky' % n)
