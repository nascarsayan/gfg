from collections import defaultdict

def areEqual(arr1, arr2):
  cnt = defaultdict(int)
  for e in arr1:
    cnt[e] += 1
  for e in arr2:
    cnt[e] -= 1
  for k in cnt.keys():
    if cnt[k] != 0:
      return 0
  return 1

t = int(input())
for i in range(t):
  n = int(input())
  arr1 = list(map(int, input().strip().split()))
  arr2 = list(map(int, input().strip().split()))
  print(areEqual(arr1, arr2))
