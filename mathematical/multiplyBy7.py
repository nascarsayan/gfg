# Multiply a number by 7
def multiply7(n):
  return (n << 3) - n

n = int(input())
print('%d * 7 = %d' % (n, multiply7(n)))
