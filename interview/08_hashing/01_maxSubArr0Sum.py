def maxLen(n, arr):
  s = 0
  l = 0
  sidx = {}
  sidx[s] = -1
  for idx in range(n):
    s += arr[idx]
    if s in sidx:
      l = max(l, idx - sidx[s])
    else:
      sidx[s] = idx
  return l


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(maxLen(n, arr))
