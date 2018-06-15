def isRotate2(s1, s2):
  if len(s1) == 1 and s1 == s2:
    return 1
  else:
    s1c = s1[-2:] + s1[:-2]
    if s1c == s2:
      return 1
    s1ac = s1[2:] + s1[:2]
    if s1ac == s2:
      return 1
  return 0

t = int(input())
for et in range(t):
  s1 = input()
  s2 = input()
  print(isRotate2(s1, s2))
