from collections import defaultdict


def get1stK(arr, n, k):
  if k > n:
    return -1
  cnt = defaultdict(int)
  for earr in arr:
    cnt[earr] += 1
  for earr in arr:
    if cnt[earr] == k:
      return earr
  return -1


t = int(input())
for i in range(t):
  n, k = list(map(int, input().strip().split()))
  arr = list(map(int, input().strip().split()))
  print(get1stK(arr, n, k))
