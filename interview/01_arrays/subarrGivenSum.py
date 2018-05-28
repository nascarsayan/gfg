def subarray(n, arr, s):
  st = 0
  fl = 0
  currS = arr[0]
  while(fl < n - 1):
    while(currS < s and fl < n - 1):
      fl += 1
      currS += arr[fl]
    while(currS > s and st < fl):
      currS -= arr[st]
      st += 1
    if currS == s:
      break
    if st == fl and fl < n - 1 and arr[fl] > s:
      fl += 1
      currS += arr[fl] - arr[st]
      st += 1
  if currS != s:
    print(-1)
  else:
    print('%d %d' % (st + 1, fl + 1))

t = int(input())
for et in range(t):
  n, s = [int(x) for x in input().split()]
  arr = [int(x) for x in input().split()]
  subarray(n, arr, s)