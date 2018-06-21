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
      while (temp.next):
        temp = temp.next
      temp.next = new_node


def createList(arr, n):
  lis = Linked_List()
  for i in range(n):
    lis.insert(arr[i])
  return lis.head


def findMid(head):
  j1 = head
  j2 = head
  while j2.next != None:
    j1 = j1.next
    j2 = j2.next
    if j2.next != None:
      j2 = j2.next
  return j1


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    head = createList(arr, n)
    print(findMid(head).data)
