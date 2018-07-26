def getPossibleChanges(coins, n, amt):
  changeArr = [[0] * (n + 1) for _ in range(amt + 1)]
  changeArr[0] = [1] * (n + 1)
  for cramt in range(1, amt + 1):
    for crcoin in range(1, n + 1):
      changeArr[cramt][crcoin] = changeArr[cramt][crcoin - 1]
      if cramt >= coins[crcoin - 1]:
        changeArr[cramt][crcoin] += changeArr[cramt -
                                              coins[crcoin - 1]][crcoin]
  return changeArr[amt][n]


t = int(input())
for _ in range(t):
  n = int(input())
  coins = list(map(int, input().strip().split()))
  amt = int(input())
  print(getPossibleChanges(coins, n, amt))
