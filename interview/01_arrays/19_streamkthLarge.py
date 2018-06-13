import heapq

def kthStream(arr, n, k):
  heap = []
  kth = []
  for idx in range(k - 1):
    heapq.heappush(heap, arr[idx])
    kth.append(-1)
  heapq.heappush(heap, arr[k - 1])
  kth.append(heap[0])
  for idx in range(k, n):
    if arr[idx] > heap[0]:
      heapq.heappushpop(heap, arr[idx])
    kth.append(heap[0])
  return kth


t = int(input())
for et in range(t):
  k, n = [int(x) for x in input().split()]
  arr = [int(x) for x in input().split()]
  print(' '.join(map(str, kthStream(arr, n, k))))
