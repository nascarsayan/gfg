def longSubstr(s1, s2, l1, l2):
  dpSub = [[0] * l2 for _ in range(l1)]
  maxLen = 0
  for i in range(l1):
    if s1[i] == s2[0]:
      dpSub[i][0] = 1
      maxLen = 1
  for j in range(l2):
    if s1[0] == s2[j]:
      dpSub[0][j] = 1
      maxLen = 1
  for i in range(1, l1):
    for j in range(1, l2):
      if s1[i] == s2[j]:
        dpSub[i][j] = dpSub[i - 1][j - 1] + 1
        maxLen = max(maxLen, dpSub[i][j])
  return maxLen


t = int(input())
for et in range(t):
  l1, l2 = [int(x) for x in input().strip().split()]
  s1 = input()
  s2 = input()
  print(longSubstr(s1, s2, l1, l2))
