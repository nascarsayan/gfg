from collections import defaultdict


def changeCnt(windowCnt, nd, val, inc):
  windowCnt[val] += inc
  if windowCnt[val] >= 1 and windowCnt[val] - inc == 0:
    nd += 1
  if windowCnt[val] == 0:
    nd -= 1
  return nd


def countDistinct(arr, n, k):
  windowCnt = defaultdict(int)
  nd = 0
  out = []
  for idx in range(min(k, n)):
    nd = changeCnt(windowCnt, nd, arr[idx], 1)
  out.append(nd)
  for idx in range(k, n):
    nd = changeCnt(windowCnt, nd, arr[idx - k], -1)
    nd = changeCnt(windowCnt, nd, arr[idx], 1)
    out.append(nd)
  print(' '.join(list(map(str, out))))


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    countDistinct(arr, n, k)
