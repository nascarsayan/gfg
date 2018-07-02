def firstDupli(s):
  for idx in range(1, len(s)):
    if s[idx] in s[:idx]:
      return s[idx]
  return -1


t = int(input())
for i in range(t):
  s = input()
  print(firstDupli(s))
