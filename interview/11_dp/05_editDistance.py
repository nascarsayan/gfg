def getEditDistance(str1, str2, n1, n2):
  distArr = [[0] * (n2 + 1) for _ in range(n1 + 1)]
  for pos1 in range(n1 + 1):
    for pos2 in range(n2 + 1):
      if pos1 == 0:
        distArr[pos1][pos2] = pos2
      elif pos2 == 0:
        distArr[pos1][pos2] = pos1
      elif str1[pos1 - 1] == str2[pos2 - 1]:
        distArr[pos1][pos2] = distArr[pos1 - 1][pos2 - 1]
      else:
        distArr[pos1][pos2] = 1 + min(distArr[pos1][pos2 - 1],
                                      distArr[pos1 - 1][pos2],
                                      distArr[pos1 - 1][pos2 - 1])
  return distArr[n1][n2]


t = int(input())
for _ in range(t):
  n1, n2 = list(map(int, input().strip().split()))
  str1, str2 = input().strip().split()
  print(getEditDistance(str1, str2, n1, n2))
