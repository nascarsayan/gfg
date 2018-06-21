# Detect if a number is divisible by 3
def check3(n):
  n = abs(n)
  if n == 0:
    return 1
  if n == 1:
    return 0
  ec = 0
  oc = 0
  while (n):
    if (n & 1):
      oc += 1
    n = n >> 1
    if (n & 1):
      ec += 1
    n = n >> 1
  return check3(oc - ec)


n = int(input())
if check3(n):
  print('%d is Multiple of 3' % n)
else:
  print('%d is not a multiple of 3' % n)
