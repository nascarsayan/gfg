def babylonSqRoot(n):
  x = n
  y = 1
  delta = 0.000001
  while(abs(x - y) > delta):
    x = (x + y) / 2
    y = n / x
  return x

n = int(input())
print('Square root of %r = %r' % (n, babylonSqRoot(n)))