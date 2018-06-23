import heapq


def getMedians(arr, n):
  maxH = []
  minH = []
  meds = []
  for idx in range(n):
    if idx % 2 == 0:
      if idx == 0 or arr[idx] <= minH[0]:
        heapq.heappush(maxH, -arr[idx])
      else:
        heapq.heappush(maxH, -heapq.heappushpop(minH, arr[idx]))
      meds.append(-maxH[0])
    else:
      if arr[idx] >= -maxH[0]:
        heapq.heappush(minH, arr[idx])
      else:
        heapq.heappush(minH, -heapq.heappushpop(maxH, -arr[idx]))
      meds.append((-maxH[0] + minH[0]) // 2)
  return meds


arr = []
n = int(input())
for i in range(n):
  arr.append(int(input()))
print('\n'.join(map(str, getMedians(arr, n))))
