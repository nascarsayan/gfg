from collections import defaultdict


def freqSort(arr, n):
  x = defaultdict(int)
  fi = []
  fo = []
  for earr in arr:
    x[earr] += 1
  for k in x.keys():
    fi.append([k, x[k]])
  fi = sorted(fi, key=lambda k: (-k[1], k[0]))
  for e in fi:
    fo = fo + [e[0]] * e[1]
  return fo


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(' '.join(map(str, freqSort(arr, n))))
