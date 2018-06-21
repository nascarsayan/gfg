def getMinIns(inp):
  l = len(inp)
  dp = [[0] * (r + 1) for r in range(l, -1, -1)]
  for j in range(2, l + 1):
    for i in range(l - j + 1):
      if inp[i] == inp[i + j - 1]:
        dp[i][j] = dp[i + 1][j - 2]
      else:
        dp[i][j] = 1 + min(dp[i + 1][j - 1], dp[i][j - 1])
  return dp[0][l]


t = int(input())
for et in range(t):
  inp = input()
  print(getMinIns(inp))
