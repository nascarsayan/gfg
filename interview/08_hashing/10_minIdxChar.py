def minIdxChar(s1, s2):
  for es1 in s1:
    if es1 in s2:
      return es1
  return 'No character present'

t = int(input())
for i in range(t):
  s1 = input()
  s2 = input()
  print(minIdxChar(s1, s2))