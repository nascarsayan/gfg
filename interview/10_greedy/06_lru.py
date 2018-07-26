def LRUFaults(arr, n, k):
  ref = []
  l = 0
  faults = 0
  for earr in arr:
    try:
      idx = ref.index(earr)
      del ref[idx]
    except ValueError:
      faults += 1
      if l == k:
        ref.pop(0)
      else:
        l += 1
    ref.append(earr)
  return faults


t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().strip().split()))
  k = int(input())
  print(LRUFaults(arr, n, k))
