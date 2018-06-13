def calcWater(arr, n):
  leftMax = [arr[0]]
  rightMax = [arr[-1]]
  for earr in arr[1:]:
    leftMax.append(max(earr, leftMax[-1]))
  for earr in reversed(arr[:-1]):
    rightMax.insert(0, max(earr, rightMax[0]))
  s = 0
  for idx in range(len(arr)):
    s += min(leftMax[idx], rightMax[idx]) - arr[idx]
  return s


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(calcWater(arr, n))
