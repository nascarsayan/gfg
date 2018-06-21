def getMedian(arr, st, size):
  tempArr = [x for x in arr[st:st + size]]
  tempArr = sorted(tempArr)
  return tempArr[size / 2]


def kthSmall(arr, n, k):
  medArr = []
  for bat in range(n / 5):
    medArr.append(getMedian(arr, bat * 5, 5))
  if (n % 5 != 0):
    medArr.append(getMedian(arr, (n / 5) * 5, n % 5))
  # kthSmall(medArr, )


t = int(input())
for et in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  k = int(input())
  print(kthSmall(arr, n, k))
