def areAnagrams(s1, s2):
  if sorted(s1) == sorted(s2):
    return 'YES'
  else:
    return 'NO'

t = int(input())
for et in range(t):
  s1 = input()
  s2 = input()
  print(areAnagrams(s1, s2))
