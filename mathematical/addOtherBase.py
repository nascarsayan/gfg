SYMMAP = list(chr(x) for x in range(ord('0'), ord('9') + 1 )) + list(chr(x) for x in range(ord('A'), ord('Z') + 1 ))

def toBaseX(n, b):
  nb = ''
  while(n):
    nb = SYMMAP[n % b] + nb
    n = int(n / b)
  return nb

def toDeci(n, b):
  p = 1
  s = 0
  for sym in reversed(n):
    s += (SYMMAP.index(sym)) * p
    p *= b
  return s

x = input().upper()
y = input().upper()
b = int(input())

x10 = toDeci(x, b)
y10 = toDeci(y, b)
print(toBaseX(x10 + y10, b))