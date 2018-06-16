def rotateList(head, k):
  currNode = head
  for _ in range(k - 1):
    currNode = currNode.next
  tmpNode = currNode
  currNode = currNode.next
  newHead = currNode
  if newHead == None:
    return head
  tmpNode.next = None
  while currNode.next != None:
    currNode = currNode.next
  currNode.next = head
  return newHead

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data, end=" ")
      temp = temp.next
    print("")

if __name__ == '__main__':
  start = LinkedList()
  t = int(input())
  while(t > 0):
    llist = LinkedList()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in reversed(values):
      llist.push(i)
    k = int(input())
    new_head = rotateList(llist.head, k)
    llist.head = new_head
    llist.printList()
    t -= 1
