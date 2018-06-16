def getNthFromLast(head, n):
  cnt = 0
  ptr = head
  while ptr != None:
    ptr = ptr.next
    cnt += 1
  ptr = head
  if cnt < n:
    return -1
  while cnt > n:
    ptr = ptr.next
    cnt -= 1
  return ptr.data

# Node Class
class node:
  def __init__(self, val):
    self.data = val
    self.next = None

# Linked List Class
class Linked_List:
  def __init__(self):
    self.head = None

  def insert(self, val):
    if self.head == None:
      self.head = node(val)
    else:
      new_node = node(val)
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = new_node

def createList(arr, n):
  lis = Linked_List()
  for i in range(n):
    lis.insert(arr[i])
  return lis.head

if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    head = createList(arr, n)
    print(getNthFromLast(head, k))
