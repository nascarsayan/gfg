import functools


def myCmp(a, b):
  sa = str(a)
  sb = str(b)
  return int(sa + sb) - int(sb + sa)


def getMaxApp(arr, n):
  return sorted(arr, key=functools.cmp_to_key(myCmp), reverse=True)


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(''.join(map(str, getMaxApp(arr, n))))
