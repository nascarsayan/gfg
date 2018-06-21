def hasPyth3(arr, n):
  sqArr = sorted([e * e for e in arr], reverse=True)
  for c in range(n - 2):
    a = c + 1
    b = n - 1
    while (a < b):
      if sqArr[a] + sqArr[b] == sqArr[c]:
        return 'Yes'
      if sqArr[a] + sqArr[b] < sqArr[c]:
        b -= 1
      else:
        a += 1
  return 'No'


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  print(hasPyth3(arr, n))
