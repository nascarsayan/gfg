def toString(l):
  return ''.join(l)


def printPermutation(a, l, r):
  if l == r:
    print(toString(a))
  else:
    for i in range(l, r + 1):
      a[l], a[i] = a[i], a[l]
      printPermutation(a, l + 1, r)
      a[l], a[i] = a[i], a[l]


aStr = input()
a = list(aStr)
print('Permutations of %s :' % aStr)
printPermutation(a, 0, len(a) - 1)
