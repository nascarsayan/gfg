def lcs(st1, st2, n1, n2):
  lcsArr = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
  for i1 in range(1, n1 + 1):
    for i2 in range(1, n2 + 1):
      if st1[i1 - 1] == st2[i2 - 1]:
        lcsArr[i1][i2] = lcsArr[i1 - 1][i2 - 1] + 1
      else:
        lcsArr[i1][i2] = max(lcsArr[i1][i2 - 1], lcsArr[i1 - 1][i2])
  # i1 = n1
  # i2 = n2
  # lcsStr = ''
  # while i1 > 0 and i2 > 0:
  #   if st1[i1 - 1] == st2[i2 - 1]:
  #     lcsStr = st1[i1 - 1] + lcsStr
  #     i1 -= 1
  #     i2 -= 1
  #   if lcsArr[i1][i2 - 1] > lcsArr[i1 - 1][i2]:
  #     i2 -= 1
  #   else:
  #     i1 -= 1
  # return lcsStr
  return lcsArr[n1][n2]


t = int(input())
for _ in range(t):
  n1, n2 = list(map(int, input().strip().split()))
  st1 = input().strip()
  st2 = input().strip()
  print(lcs(st1, st2, n1, n2))
