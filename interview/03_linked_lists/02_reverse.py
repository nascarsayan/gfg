def reverseList(self):
  # Code here
  if self.head is None:
    return None
  prevNode = self.head
  self.head = self.lastNode
  self.lastNode = prevNode
  currNode = prevNode.next

  while currNode != None:
    nextNode = currNode.next
    currNode.next = prevNode
    prevNode = currNode
    currNode = nextNode

  self.lastNode.next = None

  # rlis = Linked_List()
  # rlis.insert(self.head.data)
  # currNode = self.head.next
  # while currNode != None:
  #   new_node = node(currNode)
  #   new_node.next = rlis.head
  #   rlis.head = new_node
  #   currNode = currNode.next
  # self.head = rlis.head
  # self.lastNode = rlis.lastNode

# Node Class
class node:
  def __init__(self, val):
    self.data = val
    self.next = None

# Linked List Class


class Linked_List:
  def __init__(self):
    self.head = None
    self.lastNode = None

  def insert(self, val):
    if self.head == None:
      self.head = node(val)
      self.lastNode = self.head
    else:
      new_node = node(val)
      self.lastNode.next = new_node
      self.lastNode = new_node

  def createList(self, arr, n):
    for i in range(n):
      self.insert(arr[i])
    return self.head
  reverse_List = reverseList

  def printList(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data, end=" ")
      tmp = tmp.next
    print()

if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = Linked_List()
    head = lis.createList(arr, n)
    lis.reverse_List()
    lis.printList()
